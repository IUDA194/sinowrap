from django.shortcuts import render
from django.http import JsonResponse
from api.models import position
import requests
from django.views.decorators.csrf import csrf_exempt


class Position:
    @csrf_exempt
    def post(request) -> JsonResponse:
        if request.method == "POST": 
            request_data = request.POST
            data = {
                "name" : request_data.get("name"),
                "main_photo_path" : request_data.get("main_photo_path"),
                "description" : request_data.get("description"),
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