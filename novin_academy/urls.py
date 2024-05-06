from django.urls import path
from .views import user_input_submit
from . import views
app_name = 'academy'
urlpatterns = [
    path('academy<int:pk>/', views.home, name='team'),
    path('academy/', user_input_submit, name='academy'),
    path('details/', views.details, name='details')
]