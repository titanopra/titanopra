# admin.py
from django.contrib import admin
from .models import UserInput

class UserInputAdmin(admin.ModelAdmin):
    list_display = ('user_text',)  # نمایش متن کاربر در لیست

admin.site.register(UserInput, UserInputAdmin)
