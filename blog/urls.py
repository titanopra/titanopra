from django.urls import path

from . import views
app_name = 'w'
urlpatterns = [
    path('blog/', views.home, name='home'),
    path('blogd<int:pk>/', views.bdetail, name='blogd')
]