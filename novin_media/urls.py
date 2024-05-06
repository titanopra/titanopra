from django.urls import path

from . import views
app_name = 'media'
urlpatterns = [
    path('media/', views.home, name='home'),
    path('detail<int:pk>/', views.detail, name='detail'),
]