from django.urls import path,include
from  .views import CompanyViewSet,EmployeeViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'companies',CompanyViewSet)
router.register(r'employees',EmployeeViewset)

urlpatterns = [
    path('',include(router.urls))
    
]



#tar mane amder kache onk company ache....j companier id dibo oi comapanyr employee show korbe

#companies/{companyId}/employees