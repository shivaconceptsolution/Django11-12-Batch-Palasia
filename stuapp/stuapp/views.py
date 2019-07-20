from django.shortcuts import redirect,render
from django.http import HttpResponse
from .models import Student
def index(request):
   if request.session.has_key('uid'):
     return render(request,"stuapp/index.html")
   else:
     return redirect('/loginapp')  
def insertstudent(request):
  r = request.POST["txtrno"] 
  s = request.POST["txtname"]
  b = request.POST["txtbranch"] 
  f = request.POST["txtfees"]
  s = Student(rno=r,name=s,branch=b,fees=f)
  s.save()
  res="data inserted successfully"

  return render(request,"stuapp/index.html",{'key':res})
def viewstudent(request):
  s = Student.objects.all()  #select * from student
  return render(request,"stuapp/viewstudent.html",{'s':s})  

def editstudent(request):
  sid=request.GET["q"]
  s=Student.objects.get(pk=sid)
  return render(request,"stuapp/editstudent.html",{"key":s})
def updatestudent(request):
  i = request.POST["hid"]
  r = request.POST["txtrno"] 
  s = request.POST["txtname"]
  b = request.POST["txtbranch"] 
  f = request.POST["txtfees"]
  data = Student.objects.get(pk=i) #find
  data.rno=r
  data.name=s
  data.branch=b
  data.fees=f
  data.save()
  return redirect(viewstudent)
def deletestudent(request):
 cid=request.GET["q"]
 Student.objects.get(pk=cid).delete()
 return redirect(viewstudent)   

def logout(request):
  del request.session["uid"]
  return redirect('/loginapp')     