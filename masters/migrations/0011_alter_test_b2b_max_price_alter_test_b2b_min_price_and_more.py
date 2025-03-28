# Generated by Django 5.1.4 on 2025-03-20 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0010_remove_test_price_test_b2b_max_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='b2b_max_price',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
        migrations.AlterField(
            model_name='test',
            name='b2b_min_price',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
        migrations.AlterField(
            model_name='test',
            name='mrp',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]
