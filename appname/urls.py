from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='index'),
    path('about', views.about, name='about'),
    path('si', views.calculatesi, name='calculatesi')
]