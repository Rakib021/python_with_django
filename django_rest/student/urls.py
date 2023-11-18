from django.urls import path,include
from rest_framework import routers
from .views import Studentviewset

router = routers.DefaultRouter()
router.register(r'students',Studentviewset)


urlpatterns = [
    path('',include(router.urls))
]




