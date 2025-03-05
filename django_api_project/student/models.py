from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 30)
    roll_no = models.IntegerField()
    branch = models.CharField(max_length = 5)
    backlogs = models.CharField(max_length=10)
    percentage = models.IntegerField()
    dob = models.CharField(max_length = 15)
    email = models.EmailField()
    blood_group = models.CharField(max_length = 3)
