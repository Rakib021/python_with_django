from django.db import models

# Create your models here.

class CompanyModel(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=50,choices=(
                                            ('IT','IT'),
                                            ('MARKETING','MARKETING'),
                                            ('NON IT','NON IT'),
                                                   
                                                   ))
    
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
    
    
class EmployeeModel(models.Model):

    name = models.CharField(max_length=100)
    email =models.EmailField(max_length=50)
    address = models.CharField(max_length=100)
    phone =models.CharField(max_length=100)
    about = models.TextField()
    position =models.CharField(max_length=50,choices=(
        
        ('Manager','Manager'),
        ('Software Developer','Sd'),
        ('Project Leader','pl'),
    ))
    
    company = models.ForeignKey(CompanyModel,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
    
    