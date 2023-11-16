from django.db import models
from django.contrib.auth.models import User
    
class Lecture(models.Model):
    name=models.CharField(max_length=20)
    icon=models.ImageField()

class Degree(models.Model):
    name=models.CharField(max_length=20)
    icon=models.ImageField()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    teacher_image=models.ImageField(upload_to="images")
    degree=models.ForeignKey(Degree,on_delete=models.CASCADE,related_name="Degree_for_teachers")
    lectures=models.ManyToManyField(Lecture)
    video=models.FileField(upload_to="videos")
    manuals=models.FileField(upload_to="manuals")

class Daily(models.Model):
    property=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    group=models.IntegerField()
    lecture=models.CharField(max_length=30)
    auditorium=models.IntegerField()