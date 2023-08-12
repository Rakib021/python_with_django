from django.db import models

# Create your models here.

class StudentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=30)
    address = models.TextField()
    
    def __str__(self):
        return f"Name : {self.name}"

# Module inheritance
# 1. abstract base class
# 2. multitable inheritance
# 3. proxy model

# 1. abstract base class
class CommonInfoModel(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    class Meta:
        abstract = True
    
    


class StudentInfoModel(CommonInfoModel):
   
    section = models.CharField(max_length=20)
    roll = models.IntegerField()
    payment = models.IntegerField()
    
class TeacherInfoModel (CommonInfoModel):
    

     salary = models.IntegerField()
     
class EmployeeModel(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=40)
    designation = models.CharField(max_length=20)

class ManagerModel(EmployeeModel):
    take_interview = models.BooleanField()
    hiring = models.BooleanField()
    
class Friend(models.Model):
    school = models.CharField(max_length=20)
    section = models.CharField(max_length=10)
    attendence =models.BooleanField()
    hw = models.CharField(max_length=50)

class Myself(Friend):
    class Meta:
        proxy = True
        ordering =['-id']
    
    # One to one relationship
class Person(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    def __str__(self):
        return self.name
    
class Passport (models.Model):
    user = models.OneToOneField(to =Person,on_delete=models.CASCADE)
    pass_num = models.IntegerField()
    pass_page = models.IntegerField()
    validity = models.IntegerField()
    
# one to many

class Post(models.Model):
    user = models.ForeignKey(to=Person,on_delete=models.CASCADE,null= True)
    post_cap = models.CharField(max_length=30)
    post_details = models.CharField(max_length=30)
    
    # many to many
class Student(models.Model):
    name = models.CharField(max_length=30)
    roll = models.IntegerField()
    class_name = models.CharField(max_length=30)
    def __str__(self):
            return self.name
    
    
class Teacher(models.Model):
    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    mobile =models.CharField(max_length=40)
    
    def student_list(self):
        return ",".join([str(i) for i in  self.student.all()])
    