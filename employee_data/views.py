from django.shortcuts import render
from .models import Employee
# Create your views here.

def home(request):
	# Retrieve ALl Objects
	# emp_data=Employee.objects.all() 

	# Retrieve Specific Object
	# emp_data=Employee.objects.filter(position="Accountant")
	
	# Retrieve objects that do not match with query
	# emp_data=Employee.objects.exclude(position="Accountant")
	
	# It will order in ascending order 
	# emp_data=Employee.objects.order_by('name')

	# It will order table in descending order
	# emp_data=Employee.objects.order_by('-name')

	# It will order table in randomly manner
	# emp_data=Employee.objects.order_by('?')

	# reverse query
	emp_data=Employee.objects.order_by('id').reverse()[1:10]

	print("Return:", emp_data)
	print()
	print("SQL Query:",emp_data.query)
	return render(request,'employee_data/home.html',{'data':emp_data})