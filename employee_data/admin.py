from django.contrib import admin
from .models import Employee, HR
# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
	list_display=['id','name','email','position','city']

@admin.register(HR)
class HRAdmin(admin.ModelAdmin):
	list_display=['id','name','email','city','salary']