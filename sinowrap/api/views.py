from django.shortcuts import render
from django.http import JsonResponse
from api.models import position
import requests
from random import randint, sample
from django.views.decorators.csrf import csrf_exempt


class Position:
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
                                        width = data['width']).save()
                return JsonResponse({"status" : True})
            else:
                return JsonResponse({"status" : False, "error" : "The field cannot be null"}, status=400)
        elif request.method == "GET":
            id = request.GET.get("id")
            name = request.GET.get("name")
            if id:
                value = position.objects.filter(id=id)
                category = value[0].category
                same = position.objects.filter(category=category)
                same_data = []
                print(len(same))
                if len(same) >= 3:
                    rand_positions = sample(range(0, len(same)), 3)
                    for rand_from_same in rand_positions:
                        same_data.append({
                            "id" : same[rand_from_same].id,
                            "name" : same[rand_from_same].name,
                            "main_photo_path" : same[rand_from_same].main_photo_path,
                            "category" : same[rand_from_same].category,
                            "description" : same[rand_from_same].description,
                            "manufacturer" : same[rand_from_same].manufacturer,
                            "orign_country" : same[rand_from_same].orign_country,
                            "brand" : same[rand_from_same].brand,
                            "colors" : same[rand_from_same].colors,
                            "colors_photo_path" : same[rand_from_same].colors_photo_path,
                            "opt_price" : same[rand_from_same].opt_price,
                            "discount_price" : same[rand_from_same].discount_price,
                            "unit" : same[rand_from_same].unit,
                            "unit_storage" : same[rand_from_same].unit_storage,
                            "weight" : same[rand_from_same].weight,
                            "volume" : same[rand_from_same].volume, 
                            "length" : same[rand_from_same].length,
                            "width" : same[rand_from_same].width
                        })
                elif len(same) == 2:
                    rand_positions = sample(range(0, len(same)), 2)
                    rand_positions.append(rand_positions[0])
                    for rand_from_same in rand_positions:
                        same_data.append({
                            "id" : same[rand_from_same].id,
                            "name" : same[rand_from_same].name,
                            "main_photo_path" : same[rand_from_same].main_photo_path,
                            "category" : same[rand_from_same].category,
                            "description" : same[rand_from_same].description,
                            "manufacturer" : same[rand_from_same].manufacturer,
                            "orign_country" : same[rand_from_same].orign_country,
                            "brand" : same[rand_from_same].brand,
                            "colors" : same[rand_from_same].colors,
                            "colors_photo_path" : same[rand_from_same].colors_photo_path,
                            "opt_price" : same[rand_from_same].opt_price,
                            "discount_price" : same[rand_from_same].discount_price,
                            "unit" : same[rand_from_same].unit,
                            "unit_storage" : same[rand_from_same].unit_storage,
                            "weight" : same[rand_from_same].weight,
                            "volume" : same[rand_from_same].volume, 
                            "length" : same[rand_from_same].length,
                            "width" : same[rand_from_same].width
                        })
                elif len(same) == 1:
                    rand_positions = sample(range(0, len(same)), 1)
                    rand_positions.append(rand_positions[0])
                    rand_positions.append(rand_positions[0])
                    for rand_from_same in rand_positions:
                        same_data.append({
                            "id" : same[rand_from_same].id,
                            "name" : same[rand_from_same].name,
                            "main_photo_path" : same[rand_from_same].main_photo_path,
                            "category" : same[rand_from_same].category,
                            "description" : same[rand_from_same].description,
                            "manufacturer" : same[rand_from_same].manufacturer,
                            "orign_country" : same[rand_from_same].orign_country,
                            "brand" : same[rand_from_same].brand,
                            "colors" : same[rand_from_same].colors,
                            "colors_photo_path" : same[rand_from_same].colors_photo_path,
                            "opt_price" : same[rand_from_same].opt_price,
                            "discount_price" : same[rand_from_same].discount_price,
                            "unit" : same[rand_from_same].unit,
                            "unit_storage" : same[rand_from_same].unit_storage,
                            "weight" : same[rand_from_same].weight,
                            "volume" : same[rand_from_same].volume, 
                            "length" : same[rand_from_same].length,
                            "width" : same[rand_from_same].width
                        })
                elif len(same) == 0:
                    same_data == None

                if len(value) > 0: 
                    data = {
                    "id" : value[0].id,
                    "name" : value[0].name,
                    "main_photo_path" : value[0].main_photo_path,
                    "category" : value[0].category,
                    "description" : value[0].description,
                    "manufacturer" : value[0].manufacturer,
                    "orign_country" : value[0].orign_country,
                    "brand" : value[0].brand,
                    "colors" : value[0].colors,
                    "colors_photo_path" : value[0].colors_photo_path,
                    "opt_price" : value[0].opt_price,
                    "discount_price" : value[0].discount_price,
                    "unit" : value[0].unit,
                    "unit_storage" : value[0].unit_storage,
                    "weight" : value[0].weight,
                    "volume" : value[0].volume, 
                    "length" : value[0].length,
                    "width" : value[0].width,
                    "same" : same_data}
                    return JsonResponse({"status" : True, "data" : data})
                else: return JsonResponse({"status" : False}, status=403)
            elif name:
                value = position.objects.filter(name=name)
                if len(value) > 0: 
                    data = {
                    "id" : value[0].id,
                    "name" : value[0].name,
                    "main_photo_path" : value[0].main_photo_path,
                    "description" : value[0].description,
                    "manufacturer" : value[0].manufacturer,
                    "orign_country" : value[0].orign_country,
                    "brand" : value[0].brand,
                    "colors" : value[0].colors,
                    "colors_photo_path" : value[0].colors_photo_path,
                    "opt_price" : value[0].opt_price,
                    "discount_price" : value[0].discount_price,
                    "unit" : value[0].unit,
                    "unit_storage" : value[0].unit_storage,
                    "weight" : value[0].weight,
                    "volume" : value[0].volume, 
                    "length" : value[0].length,
                    "width" : value[0].width
                    }
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

    #получить все позиции из бд
    @csrf_exempt
    def all_positions(request) -> JsonResponse:
        if request.method == "GET":
            data = []
            data = position.objects.all()
            for obj in data:
                data.append({obj.name : {"id" : obj.id,
                                        "name" : obj.name,
                                        "main_photo_path" : obj.main_photo_path,
                                        "description" : obj.description,
                                        "manufacturer" : obj.manufacturer,
                                        "orign_country" : obj.orign_country,
                                        "brand" : obj.brand,
                                        "colors" : obj.colors,
                                        "colors_photo_path" : obj.colors_photo_path,
                                        "opt_price" : obj.opt_price,
                                        "discount_price" : obj.discount_price,
                                        "unit" : obj.unit,
                                        "unit_storage" : obj.unit_storage,
                                        "weight" : obj.weight,
                                        "volume" : obj.volume,
                                        "length" : obj.length,
                                        "width" : obj.width,
                                        "count" : 1 }})
            return JsonResponse({"status" : True,"data": data})
        elif request.method == "DELETE":
            all_data = position.objects.all()
            for obj in all_data:
                print(obj.id, "Deleted")
                obj.delete()
            return JsonResponse({"status" : True})

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
                    temp_data.append({"id" : same[rand_from_same].id,
                                "name" : same[rand_from_same].name,
                                "main_photo_path" : same[rand_from_same].main_photo_path,
                                "category" : same[rand_from_same].category,
                                "description" : same[rand_from_same].description,
                                "manufacturer" : same[rand_from_same].manufacturer,
                                "orign_country" : same[rand_from_same].orign_country,
                                "brand" : same[rand_from_same].brand,
                                "colors" : same[rand_from_same].colors,
                                "colors_photo_path" : same[rand_from_same].colors_photo_path,
                                "opt_price" : same[rand_from_same].opt_price,
                                "discount_price" : same[rand_from_same].discount_price,
                                "unit" : same[rand_from_same].unit,
                                "unit_storage" : same[rand_from_same].unit_storage,
                                "weight" : same[rand_from_same].weight,
                                "volume" : same[rand_from_same].volume, 
                                "length" : same[rand_from_same].length,
                                "width" : same[rand_from_same].width
                            })
                data.append({cat : temp_data})
            return JsonResponse({"status" : True, "data" : data})

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
                 cart : str) -> None:
        if title and name and last_name and email and phone and cart:
            if type(cart) == list:
                self.title = title
                self.name = name
                self.last_name = last_name
                self.email = email
                self.email = phone
                self.cart = cart
            else: 
                self.title = title
                self.name = name
                self.last_name = last_name
                self.email = email
                self.phone = phone
                self.cart = "Пусто"

    def send(self) -> dict:
        url = f"https://b24-haqtxw.bitrix24.ru/rest/1/tezbmobj4wl89l2y/crm.lead.add.json?FIELDS[TITLE]={self.title}&FIELDS[NAME]={self.name}&FIELDS[LAST_NAME]={self.last_name}&FIELDS[EMAIL][0][VALUE]={self.email}&FIELDS[EMAIL][0][VALUE_TYPE]=PERSONAL&FIELDS[PHONE][0][VALUE]={self.phone}&FIELDS[PHONE][0][VALUE_TYPE]=PERSONAL&FIELDS[COMMENTS]={self.cart}"
        request_data = requests.get(url)
        if request_data.status_code == 200 or request_data.status_code == "200":
            return {"status" : True}
        else: return {"status" : False, "code" : request_data.status_code}

def add_lid_to_bitrix(request) -> JsonResponse:
    if request.method == "POST": 
        request_data = request.POST
        data = {"name" : request_data.get("name"), 
                "title" : request_data.get("title"), 
                "last_name" : request_data.get("last_name"),
                "email" : request_data.get("email"),
                "phone" : request_data.get("phone"),
                "cart" : request_data.get("cart")}
        print(data)
        if data["title"] and data["name"] and data["last_name"] and data["email"] and data['phone'] and data['cart']:
            lid = bitrix_lid(title=data["title"], 
                             name=data["name"], 
                             last_name=data["last_name"], 
                             email=data['email'],
                             phone=data['phone'],
                             cart=data["cart"])
            sended = lid.send()
            if sended['status']: return JsonResponse({"status" : True}, status = 200)
            else: return JsonResponse({"status" : False  }, status = 501)
        else: return JsonResponse({"status" : False, "text" : "Bad Request"}, status = 400)

