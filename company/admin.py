from django.contrib import admin
from .models import Company
# Register your models here.
@admin.register(Company)
class CompanyModel(admin.ModelAdmin):
	list_display=['id','name','location','review']