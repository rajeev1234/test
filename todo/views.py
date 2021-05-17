from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from todo.models import *



@csrf_exempt
def employeeList(request):
    if request.method == 'GET':
        try:
          employee = Employee.objects.all()
          employeeLists = []
          for e in employee:
            obj = {}
            obj['name'] = e.name
            obj['id'] = e.id
            employeeLists.append(obj)


          return JsonResponse({
            "employee" : employeeLists,
            "Error" : "NA"
          })
        except Exception as ex:
            return JsonResponse({'Error': 'Error occured'+ str(ex)})
    return JsonResponse({'Error': 'Error occured : Not a Get method'})

@csrf_exempt
def qualificationNameList(request):
    if request.method == 'GET':
        try:
          qualification = Qualification.objects.all()
          qualificationList = []
          for e in qualification:
            obj = {}
            obj['name'] = e.qualificationName
            obj['id'] = e.id
            qualificationList.append(obj)


          return JsonResponse({
            "qualificationList" : qualificationList,
            "Error" : "NA"
          })
        except Exception as ex:
            return JsonResponse({'Error': 'Error occured'+ str(ex)})
    return JsonResponse({'Error': 'Error occured : Not a Get method'})