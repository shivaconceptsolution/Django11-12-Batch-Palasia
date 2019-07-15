from django.shortcuts import render
def index(request):
	if request.POST.get("btnadd") is not None:
		a=int(request.POST["txtnum1"])
		b=int(request.POST["txtnum2"])
		c=a+b
	if request.POST.get("btnsub") is not None:
		a=int(request.POST["txtnum1"])
		b=int(request.POST["txtnum2"])
		c=a-b
	if request.POST.get("btnmulti") is not None:
		a=int(request.POST["txtnum1"])
		b=int(request.POST["txtnum2"])
		c=a*b
	if request.POST.get("btndiv") is not None:
		a=int(request.POST["txtnum1"])
		b=int(request.POST["txtnum2"])
		c=a/b
						
	return render(request,"calcapp/index.html",{'key':c,'num1':a,'num2':b})
