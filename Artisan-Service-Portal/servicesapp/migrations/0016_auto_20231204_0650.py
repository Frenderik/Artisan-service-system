# Generated by Django 3.2 on 2023-12-04 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicesapp', '0015_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='category',
            field=models.CharField(choices=[('1', 'Masonry and concrete works'), ('2', 'Furniture and Home Decors'), ('3', 'Culinary Arts'), ('4', 'Metalwork and Plumbing Services'), ('5', 'Fine art and Painting artisans'), ('6', 'Digital arts and Designs'), ('7', 'Fashion Designs and Tailoring'), ('8', 'Glass and Ceramics'), ('9', 'Technology and Electronics')], max_length=100),
        ),
        migrations.AlterField(
            model_name='service',
            name='website',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
