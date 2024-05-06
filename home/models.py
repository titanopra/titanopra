from django.db import models

# Create your models here.
class image_slider(models.Model):
    image = models.ImageField(upload_to='')
    text = models.TextField(max_length=1000,null=True,blank=True)
    text2 = models.TextField(max_length=1000,null=True,blank=True)
    text3 = models.TextField(max_length=1000,null=True,blank=True)
    text4 = models.TextField(max_length=1000,null=True,blank=True)
    link = models.TextField(max_length=1000,null=True,blank=True)


    class Meta:
        verbose_name = "اسلایدر"
        verbose_name_plural = "عکس های صفحه اصلی"

class team_image(models.Model):
    image = models.ImageField(upload_to='')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    class Meta:
        verbose_name = "تیم"
        verbose_name_plural = "عکس های تیم"
    def __str__(self):
        return self.name



class clasS(models.Model):
    image = models.ImageField(upload_to='')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "دوره ها"
        verbose_name_plural = "دوره ها"

class Customers(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    class Meta:
        verbose_name = "نظرات"
        verbose_name_plural = "نظرات"

class Period(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        verbose_name = "جزئیات دوره ها"