from django.db import models

# Create your models here.
class Employee(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField(max_length=100)
	position=models.CharField(max_length=100)
	city=models.CharField(max_length=100)

class HR(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField(max_length=100)
	city=models.CharField(max_length=100)
	salary=models.IntegerField()