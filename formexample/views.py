from django.shortcuts import render

def index(request):  #load method
	return render(request,"formexample/index.html")
def add(request):     #action method
	a = request.GET['t']
	b = request.GET['u']
	c = int(a)+int(b)

	return render(request,"formexample/add.html",{'r':c})

