from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Employee(models.Model):
  dateCreated = models.DateTimeField(auto_now_add=True, null=True, blank=True)
  dateModified = models.DateTimeField(null=True, blank=True, default=timezone.now)
  createdBy = models.CharField(max_length=1000, null=True, blank=True)
  modifiedBy = models.CharField(max_length=1000, null=True, blank=True)
  name = models.CharField(max_length=1000,null=True,blank=True)
  dob = models.CharField(max_length=500)
  gender = models.CharField(max_length=500)
  salary = models.FloatField(max_length=500)

  def _str_(self):
    return self.name

class Qualification(models.Model):
    dateCreated = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    dateModified = models.DateTimeField(null=True, blank=True, default=timezone.now)
    createdBy = models.CharField(max_length=1000, null=True, blank=True)
    modifiedBy = models.CharField(max_length=1000, null=True, blank=True)
    qualificationName = models.CharField(max_length=1000,null= True, blank=True)


class EmployeeQualification(models.Model):
    dateCreated = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    dateModified = models.DateTimeField(null=True, blank=True, default=timezone.now)
    createdBy = models.CharField(max_length=1000, null=True, blank=True)
    modifiedBy = models.CharField(max_length=1000, null=True, blank=True)
    Qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE,null=False,blank=False)
    Employee = models.ForeignKey(Employee, on_delete=models.CASCADE,null=False,blank=False)