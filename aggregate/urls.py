from django.urls import path
from . import views

urlpatterns = [
    path('student_data/',views.stdata),
]
