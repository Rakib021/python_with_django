from django.db import models

# Create your models here.

class CourseModel(models.Model):
    course_id =models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(max_length=50)
    enrolled = models.DateTimeField(auto_now=True)
    semester = models.CharField(max_length=50,choices=(
                                                            ('semester1','semester1'),
                                                            ('semester2','semester2'),
                                                            ('semester3','semester3'),
                                                            ('semester4','semester4'),
        
                                                                ))
    
    mentors_name = models.CharField(max_length=50)
