# Generated by Django 3.2 on 2023-11-16 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0007_auto_20231114_2019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Daily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.IntegerField()),
                ('lecture', models.CharField(max_length=30)),
                ('auditorium', models.IntegerField()),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Project.userprofile')),
            ],
        ),
    ]
