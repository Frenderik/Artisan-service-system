# Generated by Django 3.2 on 2023-11-23 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_user_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
    ]
