from django.db import models

# Create your models here.

class StudentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    Fathers_name = models.CharField(max_length=20)
    address = models.TextField()
