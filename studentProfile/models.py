from django.db import models

# Create your models here.

# student

class Student(models.Model):
    
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    


class Profile(models.Model):
    
    student = models.OneToOneField(Student , on_delete=models.CASCADE, related_name="profile")
    phone = models.CharField(max_length=11)
    age = models.IntegerField()
    
    
    
    


