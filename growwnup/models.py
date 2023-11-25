from django.db import models
from django.utils.timezone import now

class Student(models.Model):
    student_id = models.AutoField
    student_name = models.CharField(max_length=25)
    student_email = models.CharField(max_length=50)
    student_wpNumber = models.IntegerField(max_length=15)
    student_intro = models.CharField(max_length=300)
    timestamp = models.DateTimeField(default=now)