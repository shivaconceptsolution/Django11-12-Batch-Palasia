from django.shortcuts import render
def index(request):
	return render(request,"primenumber/index.html")

def primelogic(request):
   num=int(request.GET["txtnum"])
   count=0
   for i in range(1,num+1):
     if num%i==0:
        count=count+1
   if count==2:
      res="Prime"
   else:
      res="NOT Prime"        	
   return render(request,"primenumber/primelogic.html",{'key':res}) 	


