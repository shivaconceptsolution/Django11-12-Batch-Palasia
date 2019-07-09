from django.shortcuts import render
from django.http import HttpResponse
def index(request):
	return render(request,"guestapp/index.html")
def about(request):
	return render(request,"guestapp/about.html")
def contact(request):
    return render(request,"guestapp/contact.html") 	

def services(request):
	return render(request,"guestapp/service.html")

