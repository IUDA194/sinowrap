import ast
import json

data_str = '[{"color_id":0,"product_id":16947,"product_name":"Ветка Оливы 绿化 6 соцветий "Агрелия" 95 см Пластик/Ткань","color_name":"Зелёный","photo_path":"71ccd860-addc-11ee-b0b2-9c6b0010f581.png","count":3,"opt_price":107.9,"total":"68.00"}]'

def formatttt_string_to_list(data : str):
    p_n = data.find("product_name")
    c_n = data.find('","color_name"')
    new_part = data[p_n+15:c_n].replace('"', '')
    datta = data.replace(data[p_n+15:c_n], new_part)
    return datta


data = ast.literal_eval(formatttt_string_to_list(data_str))


order_details = ""
total_order_amount = 0  # Variable to store the total order amount



for item in data:
    order_details = order_details + f"{item['product_name']}: {item['count']} шт.\n"
    total_order_amount += float(item['opt_price'] + item['count'])  # Sum up the total values

print(total_order_amount)