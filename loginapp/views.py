from django.shortcuts import redirect,render
from django.http import HttpResponse
from . models import Login

def index(request):
	return render(request,"loginapp/index.html")
def logincode(request):
	uname = request.POST["txtuser"]
	pass1 = request.POST["txtpass"]
	res = Login.objects.filter(username=uname,password=pass1)
	if count(res)>0:
		instance = res.values('id')[0]
		request.session["sid"]=instance['id']
		request.session["uid"]=uname
		return redirect('/stuapp')
	else:
	    return render(request,"loginapp/index.html",{'key':'invalid userid and password'}) 


def register(request):
	return render(request,"loginapp/register.html")

def regcode(request):
	uname = request.POST["txtuser"]
	pass1 = request.POST["txtpass"]
	email = request.POST["txtemail"]
	mobile = request.POST["txtmobile"]
	res = Login(username=uname,password=pass1,email=email,mobile=mobile)
	res.save()
	return render(request,"loginapp/register.html",{'key':'registration successfully'})
