# Generated by Django 3.0.4 on 2022-01-06 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myposts', '0003_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]