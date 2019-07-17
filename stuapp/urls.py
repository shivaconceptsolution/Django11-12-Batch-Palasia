from django.urls import path
from . import views

urlpatterns=[
path('',views.index,name='index'),
path('insertstudent',views.insertstudent,name='insertstudent'),
path('viewstudent',views.viewstudent,name='viewstudent')
]