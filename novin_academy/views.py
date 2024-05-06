from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.shortcuts import get_list_or_404, get_object_or_404
from django.core.paginator import Paginator
from home.models import clasS
from .models import Period,UserInput
from home .models import clasS
# Create your views here.
def home(request,pk):
    classes = clasS.objects.get(id=pk)
    period = Period.objects.filter(id=pk)
    periods = Period.objects.all()
    return render(request,'novin_academy/faqs.html',{'pk':classes,'periods':periods,'period':period})

def user_input_submit(request):
    if request.method == 'POST':
        user_text = request.POST.get('user_text','name')
        user_text1 = request.POST.get('user_text1')
        user_text2 = request.POST.get('user_text2')

        UserInput.objects.create(user_text=user_text, user_text1=user_text1, user_text2=user_text2)
        # انجام دیگر عملیات مورد نیاز

    return render(request, 'novin_academy/faqs.html')


def details(request):
    classes = clasS.objects.all()
    return render(request, 'novin_academy/menu.html',{'classes':classes})