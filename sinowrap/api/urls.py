from django.urls import path
from api.views import Position, Bitrix

urlpatterns = [
    path("positions/", Position.main_url),
    path("positions/all", Position.all_positions),
    path("positions/category", Position.get_all_category),
    path("buy/", Bitrix.url)
]
