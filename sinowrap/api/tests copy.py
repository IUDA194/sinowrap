import json

data = '[{"color_id":0,"product_id":16947,"product_name":"Ветка Оливы 绿化 6 соцветий "Агрелия" 95 см Пластик/Ткань","color_name":"Зелёный","photo_path":"71ccd860-addc-11ee-b0b2-9c6b0010f581.png","count":3,"opt_price":107.9,"total":"68.00"}]'

def formatttt_string_to_list(data):
    p_n = data.find("product_name")
    c_n = data.find('","color_name"')
    print(data[p_n+15:c_n].replace('"', ''))
    