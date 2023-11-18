from django.db import models
from base.models import BaseModel



class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,null=True,blank=True)
    category_image = models.ImageField(upload_to="categories")
    
class Car(BaseModel):
    car_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='cars')
    price = models.IntegerField()
    car_description = models.TextField()
    
class CarImage(BaseModel):
    car = models.ForeignKey(Car,on_delete=models.CASCADE,related_name='car_images')
    image = models.ImageField(upload_to ='cars')
