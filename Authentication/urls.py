from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.get_signup_page, name='signup'),
    path('signup/signupform/', views.sign_up, name='signupform'),
    path('', views.get_login_page, name='login'),
    path('login/', views.get_login_page, name='login'),
    path('login/loginform', views.login, name='loginform'),
]
