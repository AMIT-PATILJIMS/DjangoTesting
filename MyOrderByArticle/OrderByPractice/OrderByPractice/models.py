# app/models.py
from django.db import models


class EmployeeDetails(models.Model):
	EmployeeId = models.AutoField(primary_key=True)
	EmployeeName = models.CharField(max_length=20)
	EmployeeDepartment = models.CharField(max_length=20, blank=True, null=True)
	Country = models.CharField(max_length=20, blank=True, null=True)
