# Generated by Django 5.1.4 on 2025-03-30 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0026_alter_lab_mobile_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='title',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
