from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from StudentApp.models import Student
from .models import StudentSession

# Create your views here.
def home(request):
    return HttpResponse('hi we are waiting for development')


def get_students(request):
    class_id = request.GET.get('class_id')
    session = request.GET.get('session')
    
    students_obj = StudentSession.objects.filter(class_id=class_id, session=session).all()
    stu_arr=[]
    if students_obj:
        for _ in students_obj:
            stu_arr.append({'id':_.student.id,'first_name':_.student.first_name, 'last_name':_.student.last_name})

    # print(stu_arr)
    return JsonResponse({'students': list(stu_arr)})