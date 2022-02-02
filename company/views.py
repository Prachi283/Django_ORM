from django.shortcuts import render

# Create your views here.
from .models import Company

def company_data(request):
	# data=Company.objects.all()

	# exact query
	# data=Company.objects.filter(name__exact='Metalyst Forgings')

	# iexact query
	# data=Company.objects.filter(name__iexact='tata consultancy')

	# contains query
	# data=Company.objects.filter(name__contains='Y')

	# in query
	# data=Company.objects.filter(id__in=[1])
	
	# greater than gt query
	# data=Company.objects.filter(id__gt=2)

	# greater than equal to query
	# data=Company.objects.filter(id__gte=2)

	# less than query 
	# data=Company.objects.filter(id__lt=2)

	# less than equal to query
	# data=Company.objects.filter(id__lte=3)

	# startswith query
	# data=Company.objects.filter(name__startswith='t')

	# isstartswith query
	# data=Company.objects.filter(name__istartswith='t')

	# endswith query
	# data=Company.objects.filter(name__endswith='y')

	# iendswith query
	data=Company.objects.filter(name__iendswith='Y')
	print("Return:",data)
	print()
	print("SQL Query:",data.query)
	return render(request,'company/companydata.html',{'companys':data})