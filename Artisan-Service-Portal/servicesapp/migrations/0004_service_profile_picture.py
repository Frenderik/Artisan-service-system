# Generated by Django 4.2.7 on 2023-11-13 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicesapp', '0003_alter_service_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='profile_picture',
            field=models.ImageField(default='DEFAULT VALUE', upload_to='profile_pictures'),
        ),
    ]
