from django.shortcuts import render
from .models import Manager

def data(request):
	# Returns sinle object 
	# empdata=Manager.objects.get(pk=1)

	# Returns the first matched object
	# empdata=Manager.objects.first()
	# empdata=Manager.objects.order_by('name').first()

	# Returns the last matched object
	# empdata=Manager.objects.order_by('name').last()

	# Returns the latest object in the table
	# empdata=Manager.objects.latest('id')

	# Returns the earliest object in the table 
	# empdata=Manager.objects.earliest('id')
	
	# Returns true if the data exists in the query
	# empdata=Manager.objects.all()
	# print(empdata.exists())
	# empdata=Manager.objects.all()
	# one_data=Manager.objects.get(pk=1)
	# print(empdata.filter(pk=one_data.pk).exists())

	# create query
	# empdata=Manager.objects.create(name="Mamta",email="mamta@gmail.com",city="Shegaon") 

	# get_or_create()
	# empdata,created=Manager.objects.get_or_create(name="Maya",email="maya@gmail.com",city="Saswad") 
	# print(created)

	# Update method 
	# empdata=Manager.objects.filter(id=4).update(name='Rani',city='Rajapur')

	# update_or_create
	# empdata,created=Manager.objects.update_or_create(name="Mamta",email="rajaji@gmail.com",city="Shegaon")	
	# print(created)

	# bulk create query
	# objs=[
	# 	Manager(name='Shashikant',email='shashi@gmail.com',city='Nashik'),
	# 	Manager(name='Rajlaxmi',email='raja@gmail.com',city='Rajapur'),
	# 	Manager(name='Indira',email='indira@gmail.com',city='Indoor')
	# 	]
	# empdata=Manager.objects.bulk_create(objs)

	# bulk update query
	# all_data=Manager.objects.all()
	# for emp in all_data:
	# 	emp.city="Ranchi"
	# empdata=Manager.objects.bulk_update(all_data,['city'])
	
	# in_bulk query
	# empdata=Manager.objects.in_bulk([1,2])
	# print(empdata[1].name)

	# Delete all data
	# empdata=Manager.objects.all().delete()

	# Delete one record
	# empdata=Manager.objects.get(pk=3)
	# deleted=empdata.delete()

	# Delete in bulk
	# empdata=Manager.objects.filter(name="Prachi").delete()

	# Count Query
	# empdata=Manager.objects.all()
	# print(empdata.count())

	# explain(format=None,**options)
	empdata=Manager.objects.all()
	print(empdata.explain())  

	print("Return:", empdata)
	return render(request,'employee/data.html',{'emp':empdata})
