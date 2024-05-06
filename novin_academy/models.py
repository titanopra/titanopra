from django.db import models

# Create your models here.
class Period(models.Model):
    name = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    description = models.TextField()
    title2 = models.CharField(max_length=1000)
    description2 = models.TextField()
    title3 = models.CharField(max_length=1000)
    description3 = models.TextField()
    title4 = models.CharField(max_length=1000)
    description4 = models.TextField()
    video_link = models.CharField(max_length=1000)
    video_image = models.ImageField(upload_to='')
    video_title = models.CharField(max_length=1000)
    image1 = models.ImageField(upload_to='')
    image2 = models.ImageField(upload_to='')
    image3 = models.ImageField(upload_to='')
    image4 = models.ImageField(upload_to='')
    video_description = models.CharField(max_length=1000)
    video_description2 = models.CharField(max_length=1000)
    video_description3 = models.CharField(max_length=1000)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "نوین آکادمی"
        verbose_name_plural = "دوره ها "

# models.py
class UserInput(models.Model):
    user_text = models.TextField()
    user_text1 = models.TextField()
    user_text2 = models.TextField()


    def __str__(self):
        return self.user_text
    class Meta:
        verbose_name = "نوین آکادمی"
        verbose_name_plural = "درخواست های نوین "