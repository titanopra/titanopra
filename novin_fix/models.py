# models.py
from django.db import models

class UserInput(models.Model):
    user_text = models.TextField()
    user_text1 = models.TextField()
    user = models.TextField()
    user_text2 = models.TextField()
    user_text3 = models.TextField()

    def __str__(self):
        return self.user_text1


    class Meta:
        verbose_name = "نوین فیکس"
        verbose_name_plural = "درخواست های نوین فیکس"