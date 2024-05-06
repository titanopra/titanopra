from django.urls import path
from .views import shop, shop_details ,go_to_gateway_view,callback_gateway_view,search_view

app_name = 'shop'
urlpatterns = [
    path('shop/', shop, name='home'),
    path('shop_details<int:pk>/', shop_details, name='details'),
    path('go_to_gateway<int:pk>/', go_to_gateway_view ,name='go_to_gateway'),
    path('callback_gateway_view/', callback_gateway_view, name='callback_gateway'),
    path('search/', search_view, name='search'),


    # دیگر مسیرها
]
