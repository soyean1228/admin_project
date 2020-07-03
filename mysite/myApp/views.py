from django.shortcuts import render
from django.http import HttpResponse
# from .models import Employee
# from .models import Authority
# from .models import Product
# from .models import Customer
from django.db import models
from . import employee_save
from . import authority_save
from . import product_save
from . import customer_save
from . import customer_purchasing_save

def index(request):
    return render(request, 'myApp/main.html')

def insert(request, table_name):
    if(table_name == 'employee'):
        return render(request, 'myApp/employee_insert.html')
    if(table_name == 'authority'):
        authority_save.save(request)
        return render(request, 'myApp/authority_insert.html')
    if(table_name == 'product'):
        product_save.save(request)
        return render(request, 'myApp/product_insert.html')
    if(table_name == 'customer'):
        customer_save.save(request)
        return render(request, 'myApp/customer_insert.html')
    if(table_name == 'customer_purchasing'):
        customer_purchasing_save.save(request)
        return render(request, 'myApp/customer_purchasing_insert.html')
    # if(table_name == 'customer_settlement'):
    #     customer_settlement_save.save(request)
    #     return render(request, 'myApp/ccustomer_settlement_insert.html')
    # if(table_name == 'co_salesman'):
    #     co_salesman_save.save(request)
    #     return render(request, 'myApp/co_salesman_insert.html')
    # if(table_name == 'broker'):
    #     broker_save.save(request)
    #     return render(request, 'myApp/broker_insert.html')
    # if(table_name == 'sales'):
    #     sales_save.save(request)
    #     return render(request, 'myApp/sales_insert.html')
    # if(table_name == 'sales_content'):
    #     sales_content_save.save(request)
    #     return render(request, 'myApp/sales_content_insert.html')
    # if(table_name == 'approval'):
    #     approval_save.save(request)
    #     return render(request, 'myApp/approval_insert.html')
    # if(table_name == 'order'):
    #     order_save.save(request)
    #     return render(request, 'myApp/order_insert.html')
    # if(table_name == 'deposit'):
    #     deposit_save.save(request)
    #     return render(request, 'myApp/deposit_insert.html')
    # if(table_name == 'delivery'):
    #     delivery_save.save(request)
    #     return render(request, 'myApp/delivery_insert.html')

def insert_check(request, table_name):
    print(table_name)
    if(table_name == 'employee'):
        employee_save.save(request)
        return render(request, 'myApp/employee_insert.html', { "isSave" : True })
    if(table_name == 'authority'):
        authority_save.save(request)
        return render(request, 'myApp/authority_insert.html', { "isSave" : True })
    if(table_name == 'product'):
        product_save.save(request)
        return render(request, 'myApp/product_insert.html', { "isSave" : True })
    if(table_name == 'customer'):
        customer_save.save(request)
        return render(request, 'myApp/customer_insert.html', { "isSave" : True })

# def employee_check(request):
#     print("employee_check")

#     for i in range(0,5):
#         name = ''; position =''; department = ''; phone_num = ''; office_num = ''; address = ''
#         name = request.POST.get('name' + str(i),'')
#         position = request.POST.get('position'+ str(i),'')
#         department = request.POST.get('department'+ str(i), '')
#         phone_num = request.POST.get('phone_num' + str(i),'')
#         office_num = request.POST.get('office_num'+ str(i),'')
#         address = request.POST.get('address'+ str(i),'')
#         if name != '' and ( position != ''  or department != ''  or phone_num != ''  or office_num != ''  or address != '' ):
#             print("0저장")
#             employee_data = Employee(name, position, department, phone_num, office_num, address) 
#             employee_data.save()

#     print("insert_check화면")

#     return render(request, 'myApp/employee_insert.html')

# def authority_check(request):
#     print("authority_check")

#     for i in range(0,5):
#         name = ''; authority =''; 
#         name = request.POST.get('authority_name' + str(i),'')
#         authority = request.POST.get('authority_authority' + str(i), '')
#         if name != '' :
#             print("0저장")
#             authority_data = Authority(name, authority) 
#             authority_data.save()

#     return render(request, 'myApp/authority_insert.html')

def select(request):
    employee_data = Employee.objects.all() 
    authority_data = Authority.objects.all() 
    product_data = Product.objects.all() 
    customer_data = Customer.objects.all() 
    return render(request, 'myApp/select.html', { "employee_data" : employee_data, "authority_data" : authority_data })