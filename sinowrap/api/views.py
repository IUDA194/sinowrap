from django.shortcuts import render
from django.http import JsonResponse
from api.models import position
import requests
from random import randint, sample
from django.views.decorators.csrf import csrf_exempt
from math import floor,ceil
from ftplib import FTP
import os


#Методы предназначиные для структуризации и ускорения работы
class help_method:
    # Функция, которая получает значения цвета товара и генерирует нужный жсон
    def extract_colors(data, i : int = None):
        if i:
            colors_list = data[i].colors.split(";")
            colors_path = data[i].colors_photo_path.split(";")
            try: colors_total = list(map(int, data[i].color_count.split(";")))
            except: colors_total = [0] * len(colors_list)
            colors = [{
                "color_id" : j,
                "product_id" : data[i].id,
                "product_name" : data[i].name,
                "color_name": colors_list[j],
                "photo_path": colors_path[j],
                "total": colors_total[j],
                "opt_price": data[i].opt_price,
                "count": 0
                } for j in range(len(colors_list))]
            
            return colors
        elif i == 0:
            colors_list = data[i].colors.split(";")
            colors_path = data[i].colors_photo_path.split(";")
            try: colors_total = list(map(int, data[i].color_count.split(";")))
            except: colors_total = [0] * len(colors_list)
            colors = [{
                "color_id" : j,
                "product_id" : data[i].id,
                "product_name" : data[i].name,
                "color_name": colors_list[j],
                "photo_path": colors_path[j],
                "total": colors_total[j],
                "opt_price": data[i].opt_price,
                "count": 0
                } for j in range(len(colors_list))]
            
            return colors
        else:
            colors_list = data.colors.split(";")
            colors_path = data.colors_photo_path.split(";")
            try: colors_total = list(map(int, data.color_count.split(";")))
            except: colors_total = [0] * len(colors_list)
            colors = [{
                "color_id" : j,
                "product_id" : data.id,
                "product_name" : data.name,
                "color_name": colors_list[j],
                "photo_path": colors_path[j],
                "total": colors_total[j],
                "opt_price": data.opt_price,
                "count": 0
                } for j in range(len(colors_list))]
            
            return colors

    # Генерим шаблонный жсончик
    def get_data(data, colors : list, i : int = None ):
        
        result = {
                                "id": data[i].id,
                                "name": data[i].name,
                                "main_photo_path": [color["photo_path"] for color in colors],
                                "category": data[i].category,
                                "description": data[i].description,
                                "manufacturer": data[i].manufacturer,
                                "orign_country": data[i].orign_country,
                                "brand": data[i].brand,
                                "colors": colors,
                                "opt_price": data[i].opt_price,
                                "discount_price": data[i].discount_price,
                                "unit": data[i].unit,
                                "unit_storage": data[i].unit_storage,
                                "weight": data[i].weight,
                                "volume": data[i].volume,
                                "length": data[i].length,
                                "width": data[i].width,
                                "count": 1
                        }
        return result 

    # Функция скачивания фото с фтп сервера
    def photo_dw(path : str = "/sinowrap", name : str = None) -> JsonResponse:
            # Создайте объект FTP и установите соединение с сервером
            ftp = FTP('st-e.server-panel.net')
            ftp.login(user='user4681634', passwd='YSJZFbU1wukv')

            # Перейдите в нужный каталог на сервере (если необходимо)
            ftp.cwd(path)

            # Откройте файл для чтения (в режиме бинарного чтения)
            try:
                with open(f"photo/{name}", 'wb') as file:
                    # Скачайте файл с сервера и сохраните его на локальном компьютере
                    ftp.retrbinary('RETR ' + name, file.write)
            except:
                os.mkdir("photo")
                with open(f"photo/{name}", 'wb') as file:
                    # Скачайте файл с сервера и сохраните его на локальном компьютере
                    ftp.retrbinary('RETR ' + name, file.write)
            # Закройте соединение с FTP-сервером
            ftp.quit()

    # Класс для интергации битрикса
    class bitrix_lid:
        final_url = None
        title = None
        name = None
        last_name = None
        email = None
        phone = None
        cart = None

        def __init__(self,
                    title : str,
                    name : str,
                    last_name : str, 
                    email : str,
                    phone : str,
                    cart : str,
                    price : int) -> None:
            if title and name and last_name and email and phone and cart:
                    self.title = title
                    self.name = name
                    self.last_name = last_name
                    self.email = email
                    self.phone = phone
                    self.cart = cart
                    self.price = price

        def send(self) -> dict:
            url = f"https://b24-4098an.bitrix24.ru/rest/1/k5ki9yi2a4omt03n/crm.lead.add.json?FIELDS[TITLE]={self.title}&FIELDS[NAME]={self.name}&FIELDS[LAST_NAME]={self.last_name}&FIELDS[EMAIL][0][VALUE]={self.email}&FIELDS[EMAIL][0][VALUE_TYPE]=WORK&FIELDS[PHONE][0][VALUE]={self.phone}&FIELDS[PHONE][0][VALUE_TYPE]=WORK&FIELDS[OPPORTUNITY]={self.price}&FIELDS[COMMENTS]={self.cart}"
            request_data = requests.get(url)
            print(request_data.text)
            if request_data.status_code == 200 or request_data.status_code == "200":
                return {"status" : True}
            else: return {"status" : False, "code" : request_data.status_code}


#Методы связанные с товарами
class Position:

    # Основной урл для работы с моделью
    @csrf_exempt
    def main_url(request) -> JsonResponse:
        #POST -> add new position
        request_data = request.POST
        if request.method == "POST":
            if request_data.get("name") and \
               request_data.get("main_photo_path") and \
               request_data.get("description") and\
               request_data.get("category") and\
               request_data.get("manufacturer") and\
               request_data.get("orign_country") and\
               request_data.get("brand") and\
               request_data.get("colors") and\
               request_data.get("colors_photo_path") and\
               request_data.get("opt_price") and\
               request_data.get("discount_price") and\
               request_data.get("unit") and\
               request_data.get("unit_storage") and\
               request_data.get("weight") and\
               request_data.get("volume") and\
               request_data.get("length") and\
               request_data.get("width"):
                data = {
                    "name" : request_data.get("name"),
                    "main_photo_path" : request_data.get("main_photo_path"),
                    "description" : request_data.get("description"),
                    "category" : request_data.get("category"),
                    "manufacturer" : request_data.get("manufacturer"),
                    "orign_country" : request_data.get("orign_country"),
                    "brand" : request_data.get("brand"),
                    "colors" : request_data.get("colors"),
                    "colors_photo_path" : request_data.get("colors_photo_path"),
                    "opt_price" : request_data.get("opt_price"),
                    "discount_price" : request_data.get("discount_price"),
                    "unit" : request_data.get("unit"),
                    "unit_storage" : request_data.get("unit_storage"),
                    "weight" : request_data.get("weight"),
                    "volume" : request_data.get("volume"), 
                    "length" : request_data.get("length"),
                    "color_count" : request_data.get("color_count"),
                    "width" : request_data.get("width")
                }

                position.objects.create(name = data['name'],
                                        main_photo_path = data['main_photo_path'],
                                        category = data['category'],
                                        description = data['description'],
                                        manufacturer = data['manufacturer'],
                                        orign_country = data['orign_country'],
                                        brand = data['brand'],
                                        colors = data['colors'],
                                        colors_photo_path = data['colors_photo_path'],
                                        opt_price = data['opt_price'],
                                        discount_price = data['discount_price'],
                                        unit = data['unit'],
                                        unit_storage = data['unit_storage'],
                                        weight = data['weight'],
                                        volume = data['volume'],
                                        length = data['length'],
                                        color_count = data['color_count'],
                                        width = data['width']).save()
                return JsonResponse({"status" : True})
            else:
                return JsonResponse({"status" : False, "error" : "The field cannot be null"}, status=400)
        elif request.method == "GET":
            id = request.GET.get("id")
            name = request.GET.get("name")
            same_n = request.GET.get("same")
            if not same_n: same_n = 4
            else: same_n = int(same_n)
            if id:
                value = position.objects.filter(id=id)
                category = value[0].category
                same = position.objects.filter(category=category)
                same_data = []
                if len(same) >= same_n:
                    rand_positions = sample(range(0, len(same)), same_n)
                    for rand_from_same in rand_positions:
                        print(rand_from_same, rand_positions)
                        colors = help_method.extract_colors(same, rand_from_same)

                        same_data.append(help_method.get_data(same, colors, rand_from_same))
                    same_data == None
                else:
                    donthave = same_n - len(same)
                    rand_positions = sample(range(0, len(same)), len(same))
                    for i in range(donthave):
                        rand_positions.append(rand_positions[0])
                    for rand_from_same in rand_positions:
                        colors = help_method.extract_colors(same, rand_from_same)
                        same_data.append(help_method.get_data(same, colors, rand_from_same))

                if len(value) > 0: 
                    colors = help_method.extract_colors(value, 0)
                    data = help_method.get_data(value, colors, 0)
                    data["same"] = same_data
                    
                    return JsonResponse({"status" : True, "data" : data})
                else: return JsonResponse({"status" : False}, status=403)
            else: return JsonResponse({"status" : False}, status=403)
        elif request.method == "DELETE":
            id = request.GET.get("id")
            name = request.GET.get("name")
            if id:
                value = position.objects.filter(id=id).delete()
                return JsonResponse({"status" : True})
            elif name:
                value = position.objects.filter(name=name).delete()
                return JsonResponse({"status" : True})
            else: return JsonResponse({"status" : False}, status=403)

    # Урл для получения всех значений из бд
    @csrf_exempt
    def all_positions(request) -> JsonResponse:
        if request.method == "GET":
            pag = request.GET.get("pag")
            category = request.GET.get("category")
            if not pag:
                data = []
                if not category: data_temp = position.objects.all()
                else: data_temp = position.objects.filter(category=category)
                for obj in data_temp:
                    colors = help_method.extract_colors(obj)
                    data.append({           "id" : obj.id,
                                            "name" : obj.name,
                                            "main_photo_path" : [color['photo_path'] for color in colors],
                                            "category" : obj.category,
                                            "description" : obj.description,
                                            "manufacturer" : obj.manufacturer,
                                            "orign_country" : obj.orign_country,
                                            "brand" : obj.brand,
                                            "colors" : colors,
                                            "opt_price" : obj.opt_price,
                                            "discount_price" : obj.discount_price,
                                            "unit" : obj.unit,
                                            "unit_storage" : obj.unit_storage,
                                            "weight" : obj.weight,
                                            "volume" : obj.volume,
                                            "length" : obj.length,
                                            "width" : obj.width,
                                            "count" : 1 
                                            })
                return JsonResponse({"status" : True, "data": data})
            elif pag:
                page_size = request.GET.get("page_size")
                if not page_size: page_size = 10
                data = []
                if not category: data_temp = position.objects.all()
                else: data_temp = position.objects.filter(category=category)
                data_temp_len = len(position.objects.all())
                number_pages = data_temp_len / int(page_size)
                if floor(number_pages) >= int(pag):
                    start_index = int(pag) * int(page_size) - int(page_size)
                    end_index = int(page_size) * int(pag)

                    data = []

                    for i in range(start_index, end_index):
                        if i >= len(data_temp):
                            break

                        colors = help_method.extract_colors(data_temp, i)
                        product_data = help_method.get_data(data_temp, colors, i)
                        data.append(product_data)

                    return JsonResponse({"status" : True,
                                        "total_pages": ceil(number_pages),
                                        "page" : ceil(number_pages),
                                        "next" : int(pag) < ceil(number_pages),
                                        "previous" : int(pag) >= ceil(number_pages),
                                        "data" : data})
                else:
                    try:
                        start_index = int(pag) * int(page_size) - int(page_size)
                        end_index = int(page_size) * int(pag)

                        data = []

                        for i in range(start_index, end_index):
                            if i >= len(data_temp):
                                break

                            colors = help_method.extract_colors(data_temp, i)
                            product_data = help_method.get_data(data_temp, colors, i)
                            data.append(product_data)

                    except IndexError:
                        return JsonResponse({"status" : True,
                                        "total_pages": ceil(number_pages),
                                        "page" : ceil(number_pages),
                                        "next" : int(pag) < ceil(number_pages),
                                        "previous" : int(pag) >= ceil(number_pages),
                                        "data" : data})
                    else:
                        return JsonResponse({"status" : True,
                                        "total_pages": ceil(number_pages),
                                        "page" : ceil(number_pages),
                                        "next" : int(pag) < ceil(number_pages),
                                        "previous" : int(pag) >= ceil(number_pages),
                                        "data" : data})
        elif request.method == "DELETE":
            all_data = position.objects.all()
            for obj in all_data:
                obj.delete()
            return JsonResponse({"status" : True})

    # Урл для получения всех категорий из бд в удобном для фронта формате
    @csrf_exempt
    def get_all_category(request) -> JsonResponse:
        if request.method == "GET":
            data = []
            all_positions = position.objects.all()
            category = []
            for positionn in all_positions:
                category.append(positionn.category)
            category = list(set(category))
            for cat in category:
                temp_data = []
                same = position.objects.filter(category=cat)
                rand_positions = sample(range(0, len(same)), 3)
                for rand_from_same in rand_positions:
                    print(not 1)
                    colors = help_method.extract_colors(same, rand_from_same)
                    temp_data.append(help_method.get_data(same, colors, rand_from_same))
                data.append({"name" : cat,
                             "type" : cat, # eng  
                             "data" : temp_data})
            return JsonResponse({"status" : True, "data" : data})

    def photo(request):
        help_method.photo_dw(name="Image_20230918180106.png")
        return render(request, "index.html", {"path" : "Image_20230918180106.png"})


#Интеграция с битриксом (В процессе...)
class Bitrix:

    # Основной урл для работы с битриксом
    @csrf_exempt
    def url(request) -> JsonResponse:
        if request.method == "POST": 
            request_data = request.POST
            data = {"name" : request_data.get("name"), 
                    "title" : request_data.get("title"), 
                    "last_name" : request_data.get("last_name"),
                    "email" : request_data.get("email"),
                    "phone" : request_data.get("phone"),
                    "cart" : request_data.get("cart"),
                    "price" : request_data.get("price")}
            if data['phone'] and data['cart']:
                lid = help_method.bitrix_lid(title=data["title"], 
                                name=data["name"], 
                                last_name=data["last_name"], 
                                email=data['email'],
                                phone=data['phone'],
                                cart=data["cart"],
                                price=int(data["price"]))
                sended = lid.send()
                if sended['status']: return JsonResponse({"status" : True}, status = 200)
                else: return JsonResponse({"status" : False  }, status = 501)
            else: return JsonResponse({"status" : False, "text" : "Bad Request"}, status = 400)
