from django.shortcuts import render
from .models import Student
def index(request):
   return render(request,"stuapp/index.html")
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
  s = Student.objects.all()
  return render(request,"stuapp/viewstudent.html",{'s':s})        
