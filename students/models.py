from django.db import models

class Student(models.Model):
    roll_no=models.TextField()
    name=models.CharField(max_length=40)
    stud_class=models.TextField()
    department=models.TextField()
