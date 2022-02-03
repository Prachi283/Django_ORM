from django.shortcuts import render
from .models import ExamCenter,Student

def home(request):
	exam_center=ExamCenter.objects.all()
	student_data=Student.objects.all()
	print(exam_center)
	print(student_data)
	return render(request,'multitable_inheritance_app/home.html',{'centers':exam_center,'students':student_data})
