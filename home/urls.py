from django.urls import path

from . import views
app_name = 'blog'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('team/', views.team, name='team'),
    path('', views.index, name='index'),
]