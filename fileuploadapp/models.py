from django.db import models

class Myupload(models.Model):
	fname=models.CharField(max_length=500)
	fdesc=models.CharField(max_length=500)
   
