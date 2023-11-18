from django.db import models

# Create your models here.

class StudentModel(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    program = models.CharField(max_length=50)
    versity = models.TextField()
    section = models.CharField(max_length=50,choices=
                                                    ( 
                                                     ('A','A'),
                                                     ('B','B'),
                                                     ('C','C'),
        
                                                            ))
    
    admission_date = models.DateTimeField(auto_now=True)
    