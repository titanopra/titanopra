# Generated by Django 5.0.4 on 2024-04-09 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image_slider',
            name='text',
            field=models.TextField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image_slider',
            name='text2',
            field=models.TextField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image_slider',
            name='text3',
            field=models.TextField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image_slider',
            name='text4',
            field=models.TextField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
