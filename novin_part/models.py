from django.db import models

# Create your models here.
class Part(models.Model):
    name = models.CharField(max_length=1000)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    inventory = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='')
    image2 = models.ImageField(upload_to='')
    image3 = models.ImageField(upload_to='')
    image4 = models.ImageField(upload_to='')
    about = models.TextField()
    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "نوین پارت"
        verbose_name_plural = "لیست محصولات"