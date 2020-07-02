from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
from .models import Authority
from .models import Product

def index(request):
    return render(request, 'myApp/main.html')

def insert(request):
    return render(request, 'myApp/insert.html')

def select(request):
    employee_data = Employee.objects.all() 
    return render(request, 'myApp/select.html',{"employee_data" : employee_data})

def employee_check(request):
    print("employee_check")

    for i in range(0,5):
        name = ''; position =''; department = ''; phone_num = ''; office_num = ''; address = ''
        name = request.POST.get('name' + str(i),'')
        position = request.POST.get('position'+ str(i),'')
        department = request.POST.get('department'+ str(i), '')
        phone_num = request.POST.get('phone_num' + str(i),'')
        office_num = request.POST.get('office_num'+ str(i),'')
        address = request.POST.get('address'+ str(i),'')
        if name != '' and ( position != ''  or department != ''  or phone_num != ''  or office_num != ''  or address != '' ):
            print("0저장")
            employee_data = Employee(name, position, department, phone_num, office_num, address) 
            employee_data.save()

    print("insert_check화면")

    return render(request, 'myApp/insert.html')

def authority_check(request):
    print("authority_check")

    for i in range(0,5):
        name = ''; authority =''; 
        name = request.POST.get('authority_name' + str(i),'')
        authority = request.POST.get('authority_authority' + str(i), '')
        if name != '' :
            print("0저장")
            authority_data = Authority(name, authority) 
            authority_data.save()

    return render(request, 'myApp/insert.html')