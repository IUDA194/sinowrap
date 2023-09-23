from django.urls import path
from api.views import Position

urlpatterns = [
    path("positions", Position.post),
]
