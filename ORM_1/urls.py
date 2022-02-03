"""ORM_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee_data/',include('employee_data.urls')),
    path('employee/',include('employee.urls')),
    path('company/',include('company.urls')),
    path('aggregate/',include('aggregate.urls')),
    path('school_model_inheritance/',include('school_model_inheritance.urls')),
    path('multitable_inheritance_app/',include('multitable_inheritance_app.urls')),
    path('proxymodel/',include('proxymodel.urls')),
    path('model_manager/',include('model_manager.urls')),
]
