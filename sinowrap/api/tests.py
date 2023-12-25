import requests

# Замените URL на адрес вашего сервера обработки изображений
url = "http://127.0.0.1:8000/api/positions/drop_img/?name=dadasda"

# Замените 'path/to/your/image.jpg' на путь к файлу изображения на вашем компьютере
files = {'image': ('image.jpg', open('/Users/aroslavgladkij/Documents/GitHub/sinowrap/img.png', 'rb'), 'image/jpeg')}

response = requests.post(url, files=files)

print(response.text)
