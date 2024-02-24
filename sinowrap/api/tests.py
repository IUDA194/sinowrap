import ast

data_str = '[{"color_id":0,"product_id":9365,"product_name":"Набор корзин Круг 编织篮 2 шт \\"Улей\\" D16 х 15 см полиджут","color_name":"Натуральный","photo_path":"8fb23777-af55-11ee-855a-f4c88abe04c8.png","count":1,"opt_price":500.5,"total":"46.00"},{"color_id":0,"product_id":8702,"product_name":"Букет Пионов 牡丹 7 бутонов \\"Садовые\\" 70 см 10/160 шт","color_name":"Ассорти цветов","photo_path":"5f9ddf29-91c1-11ee-b0a5-ac7deb7f3205.png","count":2,"opt_price":175.5,"total":"1120.00"}]'

data = ast.literal_eval(data_str)

order_details = ""
total_order_amount = 0  # Variable to store the total order amount



for item in data:
    order_details = order_details + f"{item['product_name']}: {item['count']} шт.\n"
    total_order_amount += float(item['total'].replace(',', ''))  # Sum up the total values

print(order_details)
print(f"Total Order Amount: {total_order_amount} руб.")
