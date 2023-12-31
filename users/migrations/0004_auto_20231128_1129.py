# Generated by Django 3.2 on 2023-11-28 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0001_initial'),
        ('users', '0003_auto_20231127_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='salam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('at', models.CharField(max_length=5)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='barkod_san',
            field=models.DecimalField(blank=True, decimal_places=0, default=1, max_digits=13, verbose_name='Mugallym barkod nomeri'),
        ),
        migrations.AlterField(
            model_name='user',
            name='degree',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Degree_for_teachers', to='Project.degree', verbose_name='Mugallym derejesi'),
        ),
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Department_for_teachers', to='Project.department', verbose_name='Mugallym kafedrasy'),
        ),
        migrations.AlterField(
            model_name='user',
            name='lectures',
            field=models.ManyToManyField(default=1, to='Project.Lecture', verbose_name='Mugallym okatýan dersleri'),
        ),
        migrations.CreateModel(
            name='sagbol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gowmy', models.CharField(max_length=5)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.salam')),
            ],
        ),
    ]
