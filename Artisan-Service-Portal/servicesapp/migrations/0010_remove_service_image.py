# Generated by Django 3.2 on 2023-11-19 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicesapp', '0009_alter_service_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='image',
        ),
    ]
