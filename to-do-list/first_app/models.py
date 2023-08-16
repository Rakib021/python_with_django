from django.db import models

# Create your models here.

class TaskModel(models.Model):
   

    id =models.IntegerField(primary_key=True)
    taskTitle = models.CharField(max_length=30)
    taskDescription = models.CharField(max_length=50)
    taskStatus = models.CharField(max_length=50)
   
    
