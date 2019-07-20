from django.db import models

class Login(models.Model):
	username=models.CharField(max_length=10)
	password=models.CharField(max_length=10)
	email=models.CharField(max_length=10,default='')
	mobile=models.CharField(max_length=10,default='')
	def __str__(self):
		return self.username+","+self.password+" ,"+self.email+" "+self.mobile
