
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("student_info/<int:pk>",views.student_detail),
    path("student_info/",views.student_info),
]
