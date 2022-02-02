from django.contrib import admin
from .models import Manager
# Register your models here.
@admin.register(Manager)
class MaanagerAdmin(admin.ModelAdmin):
	list_display=['id','name','email','city']