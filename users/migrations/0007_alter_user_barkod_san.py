# Generated by Django 3.2 on 2023-11-28 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20231128_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='barkod_san',
            field=models.DecimalField(blank=True, decimal_places=0, default=1, max_digits=13, verbose_name='Mugallym barkod kody'),
        ),
    ]
