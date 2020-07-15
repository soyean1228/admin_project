from django.shortcuts import render
from django.http import HttpResponse
from django.db import models

from .models import Employee
from .models import Authority
from .models import Product
from .models import Customer
from .models import CustomerPurchasing
from .models import CustomerSettlement
from .models import CoSalesman
from .models import Broker
from .models import Sales
from .models import SalesContent
from .models import Approval
from .models import OrderData
from .models import Deposit
from .models import Delivery

from . import employee_save
from . import authority_save
from . import product_save
from . import customer_save
from . import customer_purchasing_save
from . import customer_settlement_save
from . import co_salesman_save
from . import broker_save
from . import sales_save
from . import sales_content_save
from . import delivery_save
from . import deposit_save
from . import order_save
from . import approval_save
from . import select_result

def index(request):
    return render(request, 'myApp/main.html')

def insert(request, table_name):
    if(table_name == 'employee'):
        return render(request, 'myApp/employee_insert.html')
    if(table_name == 'authority'):
        return render(request, 'myApp/authority_insert.html')
    if(table_name == 'product'):
        return render(request, 'myApp/product_insert.html')
    if(table_name == 'customer'):
        return render(request, 'myApp/customer_insert.html')
    if(table_name == 'customer_purchasing'):
        return render(request, 'myApp/customer_purchasing_insert.html')
    if(table_name == 'customer_settlement'):
        return render(request, 'myApp/customer_settlement_insert.html')
    if(table_name == 'co_salesman'):
        return render(request, 'myApp/co_salesman_insert.html')
    if(table_name == 'broker'):
        return render(request, 'myApp/broker_insert.html')
    if(table_name == 'sales'):
        return render(request, 'myApp/sales_insert.html')
    if(table_name == 'sales_content'):
        return render(request, 'myApp/sales_content_insert.html')
    if(table_name == 'approval'):
        return render(request, 'myApp/approval_insert.html')
    if(table_name == 'order'):
        return render(request, 'myApp/order_insert.html')
    if(table_name == 'deposit'):
        return render(request, 'myApp/deposit_insert.html')
    if(table_name == 'delivery'):
        return render(request, 'myApp/delivery_insert.html')

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
    if(table_name == 'customer_purchasing'):
        customer_purchasing_save.save(request)
        return render(request, 'myApp/customer_purchasing_insert.html', { "isSave" : True })
    if(table_name == 'customer_settlement'):
        customer_settlement_save.save(request)
        return render(request, 'myApp/customer_settlement_insert.html', { "isSave" : True })
    if(table_name == 'co_salesman'):
        co_salesman_save.save(request)
        return render(request, 'myApp/co_salesman_insert.html', { "isSave" : True })
    if(table_name == 'broker'):
        broker_save.save(request)
        return render(request, 'myApp/broker_insert.html', { "isSave" : True })
    if(table_name == 'sales'):
        sales_save.save(request)
        return render(request, 'myApp/sales_insert.html', { "isSave" : True })
    if(table_name == 'sales_content'):
        sales_content_save.save(request)
        return render(request, 'myApp/sales_content_insert.html', { "isSave" : True })
    if(table_name == 'approval'):
        approval_save.save(request)
        return render(request, 'myApp/approval_insert.html', { "isSave" : True })
    if(table_name == 'order'):
        order_save.save(request)
        return render(request, 'myApp/order_insert.html', { "isSave" : True })
    if(table_name == 'deposit'):
        deposit_save.save(request)
        return render(request, 'myApp/deposit_insert.html', { "isSave" : True })
    if(table_name == 'delivery'):
        delivery_save.save(request)
        return render(request, 'myApp/delivery_insert.html', { "isSave" : True })

def select(request):
    return render(request, 'myApp/select.html')

def select_result(request):
    print(request)
    employee_data = Employee.objects.all() 
    authority_data = Authority.objects.all() 
    product_data = Product.objects.all() 
    customer_data = Customer.objects.all() 
    return render(request, 'myApp/select_result.html', { "employee_data" : employee_data, "authority_data" : authority_data })