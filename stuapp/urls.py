from django.urls import path
from . import views

urlpatterns=[
path('',views.index,name='index'),
path('insertstudent',views.insertstudent,name='insertstudent'),
path('viewstudent',views.viewstudent,name='viewstudent'),
path('viewstudent1',views.viewstudent1,name='viewstudent1'),
path('editstudent',views.editstudent,name='editstudent'),
path('deletestudent',views.deletestudent,name='deletestudent'),
path('updatestudent',views.updatestudent,name='updatestudent'),
path('checkrno',views.checkrno,name='checkrno'),
path('logout',views.logout,name='logout')
]