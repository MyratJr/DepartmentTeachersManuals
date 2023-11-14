from django.db import models

class Lecture(models.Model):
    name=models.CharField(max_length=20)
    icon=models.ImageField()

class Degree(models.Model):
    name=models.CharField(max_length=20)
    icon=models.ImageField()

class Teacher(models.Model):
    name=models.CharField(max_length=50)
    teacher_image=models.ImageField(upload_to="images")
    degree=models.ForeignKey(Degree,on_delete=models.CASCADE,related_name="Degree_for_teachers")
    lectures=models.ManyToManyField(Lecture)
    video=models.FileField(upload_to="videos")
    manuals=models.FileField(upload_to="manuals")

class Daily(models.Model):
    property=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    group=models.IntegerField()
    lecture=models.CharField(max_length=30)
    auditorium=models.IntegerField()