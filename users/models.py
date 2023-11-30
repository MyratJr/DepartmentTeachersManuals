import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from io import BytesIO
from barcode.writer import ImageWriter
from django.core.files import File
import barcode
from django.core.cache import cache


o_d=models.CASCADE


class User(AbstractUser):
    avatar = models.ImageField(upload_to = "images", verbose_name = "Mugallym şahsy suraty")
    degree = models.ForeignKey("Project.Degree", on_delete = models.CASCADE, related_name = "Degree_for_teachers", verbose_name = "Mugallym derejesi")
    department = models.ForeignKey("Project.Department", on_delete = models.CASCADE, related_name = "Department_for_teachers", verbose_name = "Mugallym kafedrasy")
    lectures = models.ManyToManyField("Project.Lecture", verbose_name = "Mugallym okatýan dersleri")
    barkod_san = models.DecimalField(max_digits = 13, decimal_places = 0, default = 1, verbose_name = "Mugallym barkod kody", blank = True)
    barkod_surat = models.ImageField(upload_to = 'barcode_img/', blank = True, verbose_name = "Mugallym barkod suraty")


    def __str__(self):
        return str(f'{self.first_name} {self.last_name}')


    class Meta:
        verbose_name_plural = 'Mugallymlar'


    def save(self, *args, **kwargs):
        EAN = barcode.get_barcode_class('Code128')
        ean = EAN(f'{self.barkod_san}', writer = ImageWriter())
        buffer = BytesIO()
        ean.write(buffer, options = {"write_text": False})
        self.barkod_surat.save(str(self.username) + '.jpg', File(buffer), save = False)
        return super().save(*args, **kwargs)


class Video(models.Model):
    property = models.ForeignKey(User, on_delete = models.CASCADE, blank = True)
    title = models.CharField(max_length = 100, blank = True)
    video = models.FileField(upload_to = "videos",verbose_name = "Wideo")
    video_image = models.ImageField(upload_to = "video_images", verbose_name = "Wideo daşky suraty")
    view = models.IntegerField(default = 0)
    duration = models.DurationField(default = datetime.timedelta(seconds = 0))


    class Meta:
        verbose_name_plural = 'Mugallymyň wideo sapaklary'
        verbose_name = 'Wideo'


class Manual(models.Model):
    property = models.ForeignKey(User, on_delete = models.CASCADE, blank = True)
    manual = models.FileField(upload_to = "manuals", verbose_name = "Makala")
    manual_image = models.ImageField(upload_to = "manual_images", verbose_name = "Makala daşky suraty")
    title = models.CharField(max_length = 100, verbose_name = "Makala ady")


    class Meta:
        verbose_name_plural = 'Mugallymyň makalalary'
        verbose_name = 'Makala'


class Daily(models.Model):
    property = models.ForeignKey(User, on_delete = o_d, blank = True)
    group_1 = models.ForeignKey("Project.Group", on_delete = o_d, related_name = "Groups_for_teachers_lecture", verbose_name = "Birinji sagat okatmaly topary")
    lecture_1 = models.ForeignKey("Project.Lecture", on_delete = o_d, related_name = "Lectures_for_teachers_lecture", verbose_name = "Birinji sagat okatmaly dersi")
    auditorium_1 = models.ForeignKey("Project.Auditorium", on_delete = o_d, related_name = "Auditoriums_for_teachers_lecture", verbose_name = "Birinji sagat okatmaly auditorýasy")
    group_2 = models.ForeignKey("Project.Group",on_delete = o_d, related_name = "Groups_for_teachers_lecture_2", verbose_name = "Ikinji sagat okatmaly topary")
    lecture_2 = models.ForeignKey("Project.Lecture",on_delete = o_d, related_name = "Lectures_for_teachers_lecture_2", verbose_name = "Ikinji sagat okatmaly dersi")
    auditorium_2 = models.ForeignKey("Project.Auditorium", on_delete = o_d, related_name = "Auditoriums_for_teachers_lecture_2", verbose_name = "Ikinji sagat okatmaly auditorýasy")
    group_3 = models.ForeignKey("Project.Group", o_d, related_name = "Groups_for_teachers_lecture_3", verbose_name = "Üçünji sagat okatmaly topary")
    lecture_3 = models.ForeignKey("Project.Lecture", on_delete = o_d, related_name = "Lectures_for_teachers_lecture_3", verbose_name = "Üçünji sagat okatmaly dersi")
    auditorium_3 = models.ForeignKey("Project.Auditorium", on_delete = o_d, related_name = "Auditoriums_for_teachers_lecture_3", verbose_name = "Üçünji sagat okatmaly auditorýasy")


    def __str__(self):
        aqw = Daily.objects.filter( property = self.property)
        cached_number = cache.get('my_number')
        if cached_number is None:
            cache.set('my_number', 0)
            cached_number = cache.get('my_number')
        if cached_number == len(aqw) - 1:
            cache.delete('my_number')
        else:
            cache.set('my_number', int(cache.get('my_number')) + 1)
        days_of_week = ["Duşenbe", "Sişenbe", "Çarşenbe", "Penşenbe", "Anna", "Şenbe"]
        return str(days_of_week[cached_number])
       
    class Meta:
        verbose_name_plural = 'Mugallymyň raspisanýasy'
        verbose_name = 'Gün'