from django.urls import path
from api.views import Position, Bitrix, DRF_viewSet, DRF_viewSet_smart, collect_static, rename_static, CategoryCreateView

urlpatterns = [
    path("position/", DRF_viewSet.as_view()),
    path("position/<int:pk>/", DRF_viewSet_smart.as_view()),
    path("positions/", Position.main_url),
    path("positions/drop_img/", collect_static.as_view()),
    path("positions/all", Position.all_positions),
    path("positions/category", Position.get_all_category),
    path("positions/random", Position.get_random_id),
    path("positions/random/price", Position.get_all_category_for_price_list),
    path("buy/", Bitrix.url),
    path("rename/", rename_static.main_url),
    path("category/", CategoryCreateView.as_view())
]
