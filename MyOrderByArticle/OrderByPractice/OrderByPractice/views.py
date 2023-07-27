from django.shortcuts import render, HttpResponse
from . models import EmployeeDetails


def ShowDetails(request):
    #users = EmployeeDetails.objects.all().values()
    users = EmployeeDetails.objects.all().order_by('EmployeeName').values().reverse()
    #users = EmployeeDetails.objects.all().order_by('EmployeeName').values()
    return render(request, 'ShowEmployeeDetails.html',
                  context={'users': users})
