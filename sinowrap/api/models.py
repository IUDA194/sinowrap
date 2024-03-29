from django.db import models

class position(models.Model):
    name = models.TextField(max_length=228, default="Не указанно")
    articul = models.TextField(max_length=228, default="Не указанно")
    main_photo_path = models.TextField(max_length=1028, default="Не указанно")
    description = models.TextField(max_length=1028, default="Не указанно")
    category = models.TextField(max_length=1028, default="Не указанно")
    manufacturer = models.TextField(max_length=1028, default="Не указанно")
    orign_country = models.TextField(max_length=1028, default="Не указанно")
    brand = models.TextField(max_length=1028, default="Не указанно")
    colors = models.TextField(default="Стандартный")
    colors_photo_path = models.TextField(default="None")
    opt_price = models.FloatField(default=0)
    discount_price = models.FloatField(default=0)
    unit = models.TextField(max_length=228, default="Не указанно")
    unit_storage = models.TextField(max_length=228, default="Не указанно")
    box = models.TextField(max_length=1000, default="Не указанно")
    weight = models.FloatField(default=0)
    volume = models.FloatField(default=0)
    length = models.FloatField(default=0)
    width = models.FloatField(default=0)
    color_count = models.TextField(max_length=228, default="0;0")

class category(models.Model):
    super_category_name = models.CharField(max_length=250, default="Не указанно")
    super_category_inner = models.CharField(max_length=2500, default="Не указанно")