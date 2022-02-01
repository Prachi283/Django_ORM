from django.shortcuts import render
from .models import Employee,HR
from django.db.models import Q,F
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
	# emp_data=Employee.objects.order_by('?').values('name')

	# reverse query
	# emp_data=Employee.objects.order_by('id').reverse()[1:10]

	# Return a queryset in dictionary
	# emp_data=Employee.objects.values()

	# Retrieve Particular tables 
	# emp_data=Employee.objects.values('name','position')
 
	# Eliminate duplicate rows  
	# emp_data=Employee.objects.all().values('name').distinct()

	#  Return values in the form of tuples()
	# emp_data=Employee.objects.values_list()
	# emp_data=Employee.objects.values_list('id','name',named=True)

	# emp_data=Employee.objects.using('default')
	# emp_data=Employee.objects.dates('pass_date','month')

	# emp_data=Employee.objects.none()

	######## Second Table started #######

	# Union 
	"""
	qs1=Employee.objects.values_list('id','name',named=True)
	qs2=HR.objects.values_list('id','name',named=True)
	emp_data=qs2.union(qs1,all=True)
	"""
	"""
	qs1=Employee.objects.filter(id=5)
	qs2=Employee.objects.filter(id=6)
	emp_data=qs2.union(qs1)
	"""

	#  Intersection
	"""
	qs1=Employee.objects.values_list('id','name',named=True)
	qs2=HR.objects.values_list('id','name',named=True)
	emp_data=qs2.intersection(qs1)
	"""

	"""
	#  Difference
	qs1=Employee.objects.values_list('id','name',named=True)
	qs2=HR.objects.values_list('id','name',named=True)
	emp_data=qs1.difference(qs2)
	"""

	# AND 
	# emp_data=Employee.objects.filter(name="Prachi") & Employee.objects.filter(position="Software Engineer Trainee")
	# emp_data=Employee.objects.filter(Q(name="Prachi") & Q(position="Software Engineer Trainee"))

	# OR 
	# emp_data=Employee.objects.filter(city="Aurangabad") | Employee.objects.filter(position="Teacher")
	# emp_data=Employee.objects.filter(Q(city="Aurangabad")|Q(position="Teacher"))

	# NOT 
	# emp_data=Employee.objects.filter(~Q(position="Teacher"))

	# only(*fields)
	# emp_data=Employee.objects.filter(name__startswith="P").only('id','name')
	# emp_data=Employee.objects.filter(name__startswith="P").values('id','name')

	# filter the criteria by comparing the field values
	# emp_data=Employee.objects.filter(name=F("city"))
	


	print("Return:", emp_data)
	print()
	print("SQL Query:",emp_data.query)
	return render(request,'employee_data/home.html',{'data':emp_data})