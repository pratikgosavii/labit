# Generated by Django 5.1.4 on 2025-03-20 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0008_testimonials'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
