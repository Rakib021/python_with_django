from django.urls import path,include
from .views import home,posts,category

urlpatterns = [
    path('home/',home,name="home"),
    path('blog/<slug:url>',posts),
    path('category/<slug:url>',category,name='cat')
]
