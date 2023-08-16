from django.urls import path
from first_app.views import home,signup,user_login, profile,userLogout

urlpatterns = [
    path("",home,name="home"),
    path("signup/",signup,name="signup"),
    path("login/",user_login,name="user_login"),
    path("profile/",profile,name="profile"),
    path("logout/",userLogout,name="logout"),
]
