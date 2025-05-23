# Generated by Django 5.1.4 on 2025-03-06 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='mobile_no',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='remark',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
