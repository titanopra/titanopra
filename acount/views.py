from django.shortcuts import render,redirect
from django.shortcuts import get_list_or_404, get_object_or_404
from django.core.paginator import Paginator
# from .models import image_slider,team_image,clasS,Customers,Period
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    # تغییر در اسم یا فامیل
    if request.user.is_authenticated:
        request.user.first_name = 'mostafa'
        request.user.save()

    # برسی ورود
    if request.user.is_authenticated:
        return redirect('/')
    # فرم ورود
    elif request.method == 'POST':
        password = request.POST.get('password')
        username = request.POST.get('username')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')

    context = {'errors':[]}
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')


        if password != confirm_password:
            context['errors'].append('Passwords do not match')
            return render(request, 'acount/account.html', {})

        if User.objects.filter(username=username):
            context['errors'].append('user already exists')
            return render(request, 'acount/account.html', context)


        user = User.objects.create_user(username=username,email=email,password=password)
        login(request,user)
        return redirect('/')
    return render(request, 'acount/account.html', {})