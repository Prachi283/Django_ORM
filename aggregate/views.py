from django.shortcuts import render
from .models import Student
from django.db.models import Avg,Sum,Min, Max,Count
# Create your views here.
def stdata(request):
	data=Student.objects.all()
	average=data.aggregate(Avg('marks'))
	total=data.aggregate(Sum('marks'))
	minimum=data.aggregate(Min('marks'))
	maximum=data.aggregate(Max('marks'))
	totalcount=data.aggregate(Count('marks'))

	context={'students':data,'average':average,'total':total,'minimum':minimum,'maximum':maximum,'totalcount':totalcount}
	print(average)
	print("Return:",data)
	print()
	print("SQL Query:",data.query)
	return render(request,'aggregate/student.html',context)