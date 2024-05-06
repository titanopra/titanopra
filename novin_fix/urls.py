# from django.urls import path
#
# from . import views
# app_name = 'fix'
# urlpatterns = [
#     path('fix/', views.home, name='home'),
#     # path('detail<int:pk>/', views.detail, name='detail'),
# ]

# urls.py
from django.urls import path
from .views import user_input_submit
app_name = 'fix'
urlpatterns = [
    path('fix/', user_input_submit, name='home'),
    # دیگر مسیرها
]
