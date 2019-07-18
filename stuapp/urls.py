from django.urls import path
from . import views

urlpatterns=[
path('',views.index,name='index'),
path('insertstudent',views.insertstudent,name='insertstudent'),
path('viewstudent',views.viewstudent,name='viewstudent'),
path('editstudent',views.editstudent,name='editstudent'),
path('deletestudent',views.deletestudent,name='deletestudent'),
path('updatestudent',views.updatestudent,name='updatestudent')
]