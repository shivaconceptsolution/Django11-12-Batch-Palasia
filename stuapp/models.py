from django.db import models
class Student(models.Model):
    rno = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    branch = models.CharField(max_length=200)
    fees = models.IntegerField(max_length=200)
    def __str__(self):
    	return self.rno+","+self.name+","+self.branch+","+str(self.fees)