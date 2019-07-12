from django.urls import path
from . import views

urlpatterns=[
path('',views.index,name='index'),
path('primelogic',views.primelogic,name='primelogic')

]