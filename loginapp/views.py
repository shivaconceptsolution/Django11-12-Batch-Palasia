from django.shortcuts import redirect,render
from django.http import HttpResponse
from . models import Login

def index(request):
	return render(request,"loginapp/index.html")
def logincode(request):
	uname = request.POST["txtuser"]
	pass1 = request.POST["txtpass"]
	res = Login.objects.filter(username=uname,password=pass1)
	if len(res)>0:
		return redirect('/stuapp')
	else:
	    return render(request,"loginapp/index.html",{'key':'invalid userid and password'}) 


def register(request):
	return render(request,"loginapp/register.html")

def regcode(request):
	uname = request.POST["txtuser"]
	pass1 = request.POST["txtpass"]
	res = Login(username=uname,password=pass1)
	res.save()
	return render(request,"loginapp/register.html",{'key':'registration successfully'})
