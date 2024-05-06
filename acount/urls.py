from django.urls import path

from . import views
app_name = 'acount'
urlpatterns = [
    path('acount/', views.home, name='home')
]