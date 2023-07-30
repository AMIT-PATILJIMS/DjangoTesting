from django.shortcuts import render, HttpResponse
from . models import EmployeeDetails


def ShowDetails(request):
    #users = EmployeeDetails.objects.all().values()
    users = EmployeeDetails.objects.all().order_by('Salary','EmployeeName').values()
    #users = EmployeeDetails.objects.all().order_by('EmployeeName','Salary').values()
    return render(request, 'ShowEmployeeDetails.html',
                  context={'users': users})
