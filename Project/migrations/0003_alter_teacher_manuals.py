# Generated by Django 3.2 on 2023-11-14 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0002_alter_teacher_manuals'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='manuals',
            field=models.FileField(upload_to='manuals/'),
        ),
    ]
