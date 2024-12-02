# Generated by Django 3.2 on 2023-11-25 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicesapp', '0013_alter_service_filled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='type',
            field=models.CharField(choices=[('1', 'Contract'), ('2', 'Piecework'), ('3', 'Dailywork')], max_length=10),
        ),
    ]
