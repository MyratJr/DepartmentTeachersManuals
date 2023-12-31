# Generated by Django 3.2 on 2023-11-27 18:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': 'Mugallymlar'},
        ),
        migrations.AddField(
            model_name='user',
            name='degree',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Degree_for_teachers', to='Project.degree', verbose_name='Mugallym derejesi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Department_for_teachers', to='Project.department', verbose_name='Mugallym kafedrasy'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='lectures',
            field=models.ManyToManyField(blank=True, to='Project.Lecture', verbose_name='Mugallym okatýan dersleri'),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('video', models.FileField(upload_to='videos', verbose_name='Wideo')),
                ('video_image', models.ImageField(upload_to='video_images', verbose_name='Wideo daşky suraty')),
                ('property', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Wideo',
                'verbose_name_plural': 'Mugallymyň wideo sapaklary',
            },
        ),
        migrations.CreateModel(
            name='Manual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manual', models.FileField(upload_to='manuals', verbose_name='Makala')),
                ('manual_image', models.ImageField(upload_to='manual_images', verbose_name='Makala daşky suraty')),
                ('title', models.CharField(max_length=100, verbose_name='Makala ady')),
                ('property', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Makala',
                'verbose_name_plural': 'Mugallymyň makalalary',
            },
        ),
        migrations.CreateModel(
            name='Daily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auditorium_1', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Auditoriums_for_teachers_lecture', to='Project.auditorium', verbose_name='Birinji sagat okatmaly auditorýasy')),
                ('auditorium_2', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Auditoriums_for_teachers_lecture_2', to='Project.auditorium', verbose_name='Ikinji sagat okatmaly auditorýasy')),
                ('auditorium_3', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Auditoriums_for_teachers_lecture_3', to='Project.auditorium', verbose_name='Üçünji sagat okatmaly auditorýasy')),
                ('group_1', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Groups_for_teachers_lecture', to='Project.group', verbose_name='Birinji sagat okatmaly topary')),
                ('group_2', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Groups_for_teachers_lecture_2', to='Project.group', verbose_name='Ikinji sagat okatmaly topary')),
                ('group_3', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Groups_for_teachers_lecture_3', to='Project.group', verbose_name='Üçünji sagat okatmaly topary')),
                ('lecture_1', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Lectures_for_teachers_lecture', to='Project.lecture', verbose_name='Birinji sagat okatmaly dersi')),
                ('lecture_2', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Lectures_for_teachers_lecture_2', to='Project.lecture', verbose_name='Ikinji sagat okatmaly dersi')),
                ('lecture_3', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Lectures_for_teachers_lecture_3', to='Project.lecture', verbose_name='Üçünji sagat okatmaly dersi')),
                ('property', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Gün',
                'verbose_name_plural': 'Mugallymyň raspisanýasy',
            },
        ),
    ]
