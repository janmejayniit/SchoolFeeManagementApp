from django.shortcuts import HttpResponse, redirect, render
from .models import Student
from django.core.paginator import Paginator
from .forms import StudentForm

# Create your views here.
def home(request):
    students_obj = Student.objects.order_by('-pk').all()
    paginator = Paginator(students_obj, 20)
    page_number = request.GET.get("page")
    students_list = paginator.get_page(page_number)
    return render(request, 'StudentApp/students_list.html',{'students_list':students_list})
    # return HttpResponse('Hi this is from django world!')

def add_new(request):
    
    if request.method=='POST':
        form = StudentForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('student_list')
        else:

            return render(request, 'StudentApp/student_add.html',{'form':form})
    else:
        form = StudentForm()
        # from faker import Faker
        # import random
        # fake = Faker('en_IN')
       
        # for _ in range(500):
        #     first_name = fake.unique.first_name()
        #     last_name = fake.unique.last_name()
        #     gender = random.choice(['Male','Female','Other'])
        #     email = fake.unique.email()
        #     parents_mobile = fake.unique.phone_number()
        #     aadhar_number = fake.unique.aadhaar_id()
        #     address = fake.address()
        #     profile_pic = 'profile\Male_Avatar.jpg'
        #     admission_date = fake.date()
        
        #     student = Student(first_name=first_name, last_name=last_name, gender = gender, email = email, parents_mobile = parents_mobile, aadhar_number=aadhar_number,address=address, admission_date=admission_date)
        #     student.save()

        return render(request, 'StudentApp/student_add.html',{'form':form})

    

