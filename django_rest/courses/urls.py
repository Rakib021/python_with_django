from django.urls import path,include
from rest_framework import routers
from .views import CourseViewset

router = routers.DefaultRouter()
router.register(r'courses',CourseViewset)

urlpatterns = [
    path('',include(router.urls))
]

