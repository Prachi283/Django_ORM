from django.shortcuts import render

# Create your views here.
from .models import Student

def home(request):
	student_data=Student.students.all()
	return render(request,'model_manager/home.html',{'students':student_data})