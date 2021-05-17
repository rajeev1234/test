from django.contrib import admin
from .models import Employee,Qualification,EmployeeQualification

class EmployeeAdmin(admin.ModelAdmin):
  list_display = ('name',)
  # search_fields = ['title',]

# Register your models here.
admin.site.register(Employee, EmployeeAdmin)


class QualificationAdmin(admin.ModelAdmin):
  search_fields = ['qualificationName',]
# Register your models here.
admin.site.register(Qualification, QualificationAdmin)

class EmployeeQualificationAdmin(admin.ModelAdmin):
  search_fields = ['Qualification',]


# Register your models here.
admin.site.register(EmployeeQualification, EmployeeQualificationAdmin)