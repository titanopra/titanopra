# views.py
from django.shortcuts import render
from .models import UserInput

def user_input_submit(request):
    if request.method == 'POST':
        user_text = request.POST.get('user_text','name')
        user = request.POST.get('user')
        user_text1 = request.POST.get('user_text1')
        user_text2 = request.POST.get('user_text2')
        user_text3 = request.POST.get('user_text3')

        UserInput.objects.create(user_text=user_text, user_text1=user_text1, user_text2=user_text2, user_text3=user_text3, user=user)
        # انجام دیگر عملیات مورد نیاز

    return render(request, 'novin_fix/contact.html')
