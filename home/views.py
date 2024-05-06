from django.shortcuts import render,redirect
from django.shortcuts import get_list_or_404, get_object_or_404
from django.core.paginator import Paginator
from .models import image_slider,team_image,clasS,Customers,Period
# Create your views here.
def home(request):
    images = image_slider.objects.all()
    teams = team_image.objects.all()
    classes = clasS.objects.all()
    cus = Customers.objects.all()
    return render(request, 'home/index.html', {'images': images, 'teams': teams ,'classes':classes,'cus':cus})

def team(request):
    teams = team_image.objects.all()
    return render(request,'home/our-team.html',{'teams': teams})

def index(request):
    return render(request, 'home/home.html')