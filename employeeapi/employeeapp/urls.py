from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployeeDetails.as_view()),
    path('<int:id>', views.EmployeeDetails.as_view()),
]