# Generated by Django 5.1.4 on 2025-03-25 21:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0010_remove_lab_test_address'),
        ('masters', '0024_lab_mobile_no'),
        ('order', '0011_cart_is_labitnow'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='is_labitnow',
        ),
        migrations.RemoveField(
            model_name='order',
            name='lab_test',
        ),
        migrations.RemoveField(
            model_name='order',
            name='medicine',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('collected_from_customer', 'Collected From Customer'), ('delivered_to_hub', 'Delivered To Hub'), ('collected_from_vendor', 'Collected From Vendor'), ('delivered_to_vendor', 'Delivered To Vendor'), ('cancelled', 'Cancelled')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.CreateModel(
            name='order_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('test', 'Test'), ('medicine', 'Medicine')], max_length=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('is_labitnow', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('lab_test', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lab.lab_test')),
                ('medicine', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='masters.medicine')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='order.order')),
            ],
        ),
    ]
