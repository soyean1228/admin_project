from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
from .forms import EmployeeForm

def index(request):
    return render(request, 'myApp/main.html')

def insert(request):
    return render(request, 'myApp/insert.html')

def select(request):
    employee_data = Employee.objects.all() 
    return render(request, 'myApp/select.html',{"employee_data" : employee_data})

def insert_check(request):
    print("insert_check화면")

    name = ''; position =''; department = ''; phone_num = ''; office_num = ''; address = '' 
    name = request.POST.get('name0','')
    position = request.POST.get('position0','')
    department = request.POST.get('department0','')
    phone_num = request.POST.get('phone_num0','')
    office_num = request.POST.get('office_num0','')
    address = request.POST.get('address0','')
    if name != '' and ( position != ''  or department != ''  or phone_num != ''  or office_num != ''  or address != '' ):
        print("0저장")
        employee = Employee(name, position, department, phone_num, office_num, address) 
        employee.save()

    name = ''; position =''; department = ''; phone_num = ''; office_num = ''; address = '' 
    name = request.POST.get('name1','')
    position = request.POST.get('position1','')
    department = request.POST.get('department1','')
    phone_num = request.POST.get('phone_num1','')
    office_num = request.POST.get('office_num1','')
    address = request.POST.get('address1','')
    if name != '' and ( position != ''  or department != ''  or phone_num != ''  or office_num != ''  or address != '' ):
        print("1저장")
        employee = Employee(name, position, department, phone_num, office_num, address) 
        employee.save()

    name = ''; position =''; department = ''; phone_num = ''; office_num = ''; address = '' 
    name = request.POST.get('name2','')
    position = request.POST.get('position2','')
    department = request.POST.get('department2','')
    phone_num = request.POST.get('phone_num2','')
    office_num = request.POST.get('office_num2','')
    address = request.POST.get('address2','')
    if name != '' and ( position != ''  or department != ''  or phone_num != ''  or office_num != ''  or address != '' ):
        print("2저장")
        employee = Employee(name, position, department, phone_num, office_num, address) 
        employee.save()

    name = ''; position =''; department = ''; phone_num = ''; office_num = ''; address = '' 
    name = request.POST.get('name3','')
    position = request.POST.get('position3','')
    department = request.POST.get('department3','')
    phone_num = request.POST.get('phone_num3','')
    office_num = request.POST.get('office_num3','')
    address = request.POST.get('address3','')
    if name != '' and ( position != ''  or department != ''  or phone_num != ''  or office_num != ''  or address != '' ):
        print("3저장")
        employee = Employee(name, position, department, phone_num, office_num, address) 
        employee.save()

    name = ''; position =''; department = ''; phone_num = ''; office_num = ''; address = '' 
    name = request.POST.get('name4','')
    position = request.POST.get('position4','')
    department = request.POST.get('department4','')
    phone_num = request.POST.get('phone_num4','')
    office_num = request.POST.get('office_num4','')
    address = request.POST.get('address4','')
    if name != '' and ( position != ''  or department != ''  or phone_num != ''  or office_num != ''  or address != '' ):
        print("4저장")
        employee = Employee(name, position, department, phone_num, office_num, address) 
        employee.save()

    return render(request, 'myApp/insert.html')