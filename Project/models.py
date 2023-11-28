from django.core.validators import MaxValueValidator
from django.db import models
    
class Lecture(models.Model):
    name=models.CharField(max_length=100,verbose_name="Ders ady")
    icon=models.ImageField(verbose_name="Ders suraty",upload_to="Lecture_image")

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name_plural = 'Dersler'

class Group(models.Model):
    name=models.IntegerField(verbose_name="Topar no")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = 'Toparlar'
    
class Degree(models.Model):
    name=models.CharField(max_length=20,verbose_name="Dereje")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = 'Derejeler'

class Department(models.Model):
    name=models.CharField(max_length=100,verbose_name="Kafedra")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = 'Kafedralar'

class Auditorium(models.Model):
    name=models.IntegerField(validators=[MaxValueValidator(9999)],verbose_name="Auditoriýa no")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = 'Auditorýalar'