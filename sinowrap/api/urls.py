from django.urls import path
from api.views import Position

urlpatterns = [
    path("positions/", Position.main_url),
    path("positions/all", Position.all_positions),
]