from django.db import models

class Blog(models.Model):
    image = models.ImageField(upload_to='')
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "پست ها"
        verbose_name_plural = "وبلاگ ها"

class Blog_details(models.Model):
    image = models.ImageField(upload_to='')
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=10000000)
    writer = models.CharField(max_length=100)
    writer_details = models.CharField(max_length=200)
    writer_image = models.ImageField(upload_to='')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "جرئیات"
        verbose_name_plural = "جرئیات وبلاگ ها"

class Blog_tags(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name = "تگ ها"
        verbose_name_plural = "تگ ها"