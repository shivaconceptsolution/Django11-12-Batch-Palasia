from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import Myupload
def index(request):
   if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        s = Myupload(fname=myfile.name,fdesc='only for test ')
        s.save()
        return render(request, 'fileuploadapp/index.html', {
            'key': uploaded_file_url
        })

   return render(request,"fileuploadapp/index.html")

def gallery(request):
    s= Myupload.objects.all()
    return render(request,"fileuploadapp/viewfile.html",{'key':s})   
