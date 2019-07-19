from django.db import models

class Login(models.Model):
	username=models.CharField(max_length=10)
	password=models.CharField(max_length=10)
	def __str__(self):
		return self.username+","+self.password
