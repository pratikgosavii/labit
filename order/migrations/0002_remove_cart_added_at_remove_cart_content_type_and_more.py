# Generated by Django 5.1.4 on 2025-03-16 13:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0007_medicine_category_medicine'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='added_at',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='object_id',
        ),
        migrations.AddField(
            model_name='cart',
            name='medicine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='masters.medicine'),
        ),
        migrations.AddField(
            model_name='cart',
            name='test',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='masters.test'),
        ),
        migrations.AddField(
            model_name='cart',
            name='type',
            field=models.CharField(choices=[('test', 'Test'), ('medicine', 'Medicine')], default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
