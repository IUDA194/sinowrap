from rest_framework import serializers
from api.models import position, category

class position_serializers(serializers.ModelSerializer):
    class Meta:
        model = position
        fields = ['name', 
                  "articul", 
                  "main_photo_path", 
                  "description", 
                  "category", 
                  "manufacturer",
                  "orign_country",
                  "brand",
                  "colors", 
                  "colors_photo_path",
                  "opt_price",
                  "discount_price",
                  "unit",
                  "unit_storage",
                  "weight",
                  "volume",
                  "length",
                  "width",
                  "box",
                  "color_count"]
        

class image_serializers(serializers.Serializer):
    image = serializers.CharField()
    name = serializers.CharField()

from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    super_category_inner = serializers.ListField(child=serializers.CharField(), write_only=True)
    subcategories = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = category
        fields = ['super_category_name', 'super_category_inner', "subcategories"]

    def create(self, validated_data):
        super_category_inner = validated_data.pop('super_category_inner', [])
        instance = super().create(validated_data)
        instance.super_category_inner = ';'.join(super_category_inner)
        instance.save()
        return instance
    
    def get_subcategories(self, obj):
        # Фильтруем только подкатегории, если это не главная категория
        if obj.super_category_name != "Main category name":
            subcategories = set(obj.super_category_inner.split(';'))  # Используем set для удаления дубликатов
            return [{'subcategory_name': name} for name in subcategories]
        return None  # Возвращаем None для главной категории

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['subcategories'] is None:
            del data['super_category_name']
            data['subcategories'] = []
        return data
