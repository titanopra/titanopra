from django.db import models

# Create your models here.
class Media(models.Model):
    image = models.ImageField(upload_to='')
    title = models.CharField(max_length=100)
    model = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    date = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.model
    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "موبایل های و محصولات"

class Detail_media(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=10000,blank=True)
    image = models.ImageField(upload_to='')
    image2 = models.ImageField(upload_to='')
    title2 = models.CharField(max_length=100, blank=True)
    description2 = models.TextField(max_length=10000,blank=True)
    cpu= models.CharField(max_length=10000,blank=True)
    display= models.CharField(max_length=10000,blank=True)
    camera= models.CharField(max_length=10000,blank=True)
    ram= models.CharField(max_length=10000,blank=True)
    Memory= models.CharField(max_length=10000,blank=True)
    os= models.CharField(max_length=10000,blank=True)
    Sensors= models.CharField(max_length=10000,blank=True)
    Physical_characteristics= models.CharField(max_length=10000,blank=True)
    battry= models.CharField(max_length=10000,blank=True)
    audio_and_video= models.CharField(max_length=10000,blank=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "جرئیات"
        verbose_name_plural = "جرئیات موبایل ها و محصولات"