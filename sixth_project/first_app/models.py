from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField(primary_key=True)
    fathers_name = models.TextField(default='Rakib')
    address = models.TextField()
    
    def __str__(self):
        return f"Roll:{self.roll} name: {self.name}"

