from django.urls import path
from . import views 
urlpatterns = [
    path('modelschool/',views.home),
]
