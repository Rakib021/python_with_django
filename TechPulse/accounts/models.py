from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class Teacher(AbstractUser):
    # Teacher-specific fields if needed
    is_teacher = models.BooleanField(default=True)

class Student(AbstractUser):
    # Student-specific fields if needed
    is_student = models.BooleanField(default=True)
