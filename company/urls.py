from django.urls import path
from . import views

urlpatterns = [
    path('company_data/',views.company_data),
]
