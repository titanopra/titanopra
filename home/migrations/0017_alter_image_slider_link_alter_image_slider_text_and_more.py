# Generated by Django 5.0.4 on 2024-04-28 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_image_slider_link_alter_image_slider_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_slider',
            name='link',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='image_slider',
            name='text',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='image_slider',
            name='text2',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='image_slider',
            name='text3',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='image_slider',
            name='text4',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
