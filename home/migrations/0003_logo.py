# Generated by Django 5.0.4 on 2024-04-09 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_image_slider_text_image_slider_text2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
