from rest_framework import serializers
from api.models import position

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
                  "color_count"]
        

class image_serializers(serializers.ModelSerializer):
    image = serializers.CharField()
    name = serializers.CharField()