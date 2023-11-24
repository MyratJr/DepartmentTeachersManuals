from django.core.validators import MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
    
class Lecture(models.Model):
    name=models.CharField(max_length=20)
    icon=models.ImageField()

    def __str__(self):
        return str(self.name)

class Group(models.Model):
    name=models.IntegerField()

    def __str__(self):
        return str(self.name)
    
class Degree(models.Model):
    name=models.CharField(max_length=20)
    icon=models.ImageField()

    def __str__(self):
        return str(self.name)

class Auditorium(models.Model):
    name=models.IntegerField(validators=[MaxValueValidator(9999)])

    def __str__(self):
        return str(self.name)

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    teacher_image=models.ImageField(upload_to="images")
    degree=models.ForeignKey(Degree,on_delete=models.CASCADE,related_name="Degree_for_teachers")
    lectures=models.ManyToManyField(Lecture)
    manuals=models.FileField(upload_to="manuals")

    def __str__(self):
        return str(self.user)

class Video(models.Model):
    property=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    video=models.FileField(upload_to="videos")


class Daily(models.Model):
    property=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    group=models.ForeignKey(Group,on_delete=models.CASCADE,related_name="Groups_for_teachers_lecture")
    lecture=models.ForeignKey(Lecture,on_delete=models.CASCADE,related_name="Lectures_for_teachers_lecture")
    auditorium=models.ForeignKey(Auditorium,on_delete=models.CASCADE,related_name="Auditoriums_for_teachers_lecture")