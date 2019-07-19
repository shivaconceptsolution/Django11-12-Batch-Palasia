from django.urls import path
from . import views

urlpatterns=[
path('',views.index,name='index'),
path('logincode',views.logincode,name='logincode'),
path('register',views.register,name='register'),
path('regcode',views.regcode,name='regcode')

]