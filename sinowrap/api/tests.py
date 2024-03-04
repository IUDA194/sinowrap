import ast
import json

data_str = '[{"color_id":0,"product_id":19491,"product_name":"Лента атласная 单色螺纹 2,5 см х 91 м \Однотон\","color_name":"Белый 029","photo_path":"79b8b12e-99ed-11ee-b0ac-ac7deb7f3205.png","count":1,"opt_price":188.5,"total":"11.00"},{"color_id":0,"product_id":18924,"product_name":"Букет Роз 玫瑰花束 7 бутонов \Крупная\ 65 см 20/240 шт","color_name":"Ассорти","photo_path":"70103ac8-ab7a-11ee-b0b1-9c6b0010f581.png","count":1,"opt_price":112.45,"total":"440.00"},{"color_id":0,"product_id":18857,"product_name":"Букет Георгин 芍药花束 7 бутонов \Папоротник и выскочки\ 35 см 40/800 шт","color_name":"Ассорти","photo_path":"d79cdcd5-b507-11ee-855d-f4c88abe04c8.png","count":1,"opt_price":42.9,"total":"880.00"},{"color_id":0,"product_id":18870,"product_name":"Букет Калл 马蹄莲花束 6 бутонов \Череда\ 45 см 40/1400 шт","color_name":"Ассорти","photo_path":"88850d05-a1f8-11ee-b0ad-ac7deb7f3205.png","count":2,"opt_price":37.05,"total":"2680.00"},{"color_id":0,"product_id":19819,"product_name":"Нож флористический  花泥刀 36 х 6 см","color_name":"Оранжевый","photo_path":"c0aa2cb0-94b7-11ee-b0ab-ac7deb7f3205.png","count":1,"opt_price":195,"total":"25.00"},{"color_id":0,"product_id":19053,"product_name":"Ваза стекло Геометрия 玻璃花瓶 \Леденец\ D5 х 19 см","color_name":"Зелёный","photo_path":"54f732cb-b5a8-11ee-855d-f4c88abe04c8.png","count":1,"opt_price":890.5,"total":"10.00"}]'

def find_product_name_positions(data_str: str):
    positions = []
    start = 0
    while True:
        pos = data_str.find("product_name", start)
        if pos == -1:
            break
        positions.append(pos)
        start = pos + 1
    return positions

def find_product_color_positions(data_str: str):
    positions = []
    start = 0
    while True:
        pos = data_str.find('","color_name"', start)
        if pos == -1:
            break
        positions.append(pos)
        start = pos + 1
    return positions


def formatttt_string_to_list(data : str):
        datta = data
        p_n = find_product_name_positions(data)
        c_n = find_product_color_positions(data)
        for i in range(len(p_n)):
            print(i)
            new_part = data[p_n[i]+15:c_n[i]].replace('"', '')
            print(new_part)
            datta = datta.replace(data[p_n[i]+15:c_n[i]], new_part)
        datta = datta.replace('\\', "")
        return datta

print(find_product_name_positions(data_str))
data = ast.literal_eval(formatttt_string_to_list(data_str))
print(data)
print(type(data))

order_details = ""
total_order_amount = 0  # Variable to store the total order amount



for item in data:
    order_details = order_details + f"{item['product_name']}: {item['count']} шт.\n"
    total_order_amount += float(item['opt_price'] + item['count'])  # Sum up the total values

print(total_order_amount)