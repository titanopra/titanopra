# Generated by Django 5.0.4 on 2024-04-12 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=10000000)),
                ('writer', models.CharField(max_length=100)),
                ('writer_details', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='blog_tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
