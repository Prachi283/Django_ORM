from django.db import models
from .managers import CustomManager


class Student(models.Model):
	name=models.CharField(max_length=100)
	roll=models.IntegerField()
	# objects=models.Manager()==> by default


	# Change ModelManager Name
	# students=models.Manager()


	students=CustomManager()