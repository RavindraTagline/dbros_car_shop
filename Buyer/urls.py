from django.urls import path

from .views import UserLogin, UserLogout, UserSignup

urlpatterns = [

    path('signup/', UserSignup.as_view(), name="signup"),
    path('login/', UserLogin.as_view(), name="login"),
    path('logout/', UserLogout, name="logout"),
]
