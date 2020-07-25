from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from openpyxl import load_workbook
from openpyxl import Workbook
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from .forms import UploadOrderFileModel

from .models import Employee
from .models import SamsungCode
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
from . import samsung_code_save
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
from . import scm_select

def index(request):
    return render(request, 'myApp/select.html')

def insert(request, table_name):
    if(table_name == 'employee'):
        employee_data = Employee.objects.all() 
        return render(request, 'myApp/employee.html', { "employee_data" : employee_data })
    if(table_name == 'samsung_code'):
        samsung_code_data = SamsungCode.objects.all() 
        return render(request, 'myApp/samsung_code.html', { "samsung_code_data" : samsung_code_data })
    if(table_name == 'product'):
        product_data = Product.objects.all()
        return render(request, 'myApp/product.html', { "product_data" : product_data })   
    if(table_name == 'broker'):
        broker_data = Broker.objects.all()
        return render(request, 'myApp/broker.html', { "broker_data" : broker_data })   
    if(table_name == 'customer'):
        customer_data = Customer.objects.all()
        return render(request, 'myApp/customer.html', { "customer_data" : customer_data })   
    if(table_name == 'authority'):
        return render(request, 'myApp/authority_insert.html')
    if(table_name == 'customer_purchasing'):
        return render(request, 'myApp/customer_purchasing_insert.html')
    if(table_name == 'customer_settlement'):
        return render(request, 'myApp/customer_settlement_insert.html')
    if(table_name == 'co_salesman'):
        return render(request, 'myApp/co_salesman_insert.html')
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
        isSuccess = employee_save.save(request)
        employee_data = Employee.objects.all() 
        return render(request, 'myApp/employee.html', { "isSave" : isSuccess , "employee_data" : employee_data })
    if(table_name == 'samsung_code'):
        isSuccess = samsung_code_save.save(request)
        samsung_code_data = SamsungCode.objects.all() 
        return render(request, 'myApp/samsung_code.html', { "isSave" : True , "samsung_code_data" : samsung_code_data })
    if(table_name == 'product'):
        isSuccess = product_save.save(request)
        product_data = Product.objects.all()
        return render(request, 'myApp/product.html', { "isSave" : isSuccess , "product_data" : product_data })
    if(table_name == 'broker'):
        isSuccess = broker_save.save(request)
        broker_data = Broker.objects.all()
        return render(request, 'myApp/broker.html', { "isSave" : True , "broker_data" : broker_data }) 
    if(table_name == 'customer'):
        isSuccess = customer_save.save(request)
        customer_data = Customer.objects.all()
        return render(request, 'myApp/customer.html', { "isSave" : True , "customer_data" : customer_data }) 
    if(table_name == 'authority'):
        authority_save.save(request)
        return render(request, 'myApp/authority_insert.html', { "isSave" : True })
    if(table_name == 'customer_purchasing'):
        customer_purchasing_save.save(request)
        return render(request, 'myApp/customer_purchasing_insert.html', { "isSave" : True })
    if(table_name == 'customer_settlement'):
        customer_settlement_save.save(request)
        return render(request, 'myApp/customer_settlement_insert.html', { "isSave" : True })
    if(table_name == 'co_salesman'):
        co_salesman_save.save(request)
        return render(request, 'myApp/co_salesman_insert.html', { "isSave" : True }) 
    if(table_name == 'sales'):
        sales_save.save(request)
        return render(request, 'myApp/sales_insert.html', { "isSave" : True })
    if(table_name == 'sales_content'):
        try: 
            sales_content_save.save(request)
            return render(request, 'myApp/sales_content_insert.html', { "isSave" : True })
        except IntegrityError as e:
            return render(request, 'myApp/sales_content_insert.html', { "isIntegrity" : True })
    if(table_name == 'approval'):
        try: 
            approval_save.save(request)
            return render(request, 'myApp/approval_insert.html', { "isSave" : True })
        except IntegrityError as e:
            return render(request, 'myApp/approval_insert.html', { "isIntegrity" : True })
    if(table_name == 'order'):
        try: 
            order_save.save(request)
            return render(request, 'myApp/order_insert.html', { "isSave" : True })
        except IntegrityError as e:
            return render(request, 'myApp/order_insert.html', { "isIntegrity" : True })
    if(table_name == 'deposit'):
        try: 
            deposit_save.save(request)
            return render(request, 'myApp/deposit_insert.html', { "isSave" : True })
        except IntegrityError as e:
            return render(request, 'myApp/deposit_insert.html', { "isIntegrity" : True })
    if(table_name == 'delivery'):
        try: 
            delivery_save.save(request)
            return render(request, 'myApp/delivery_insert.html', { "isSave" : True })
        except IntegrityError as e:
            return render(request, 'myApp/delivery_insert.html', { "isIntegrity" : True })

def upload(request, table_name):
    print(table_name)
    if(table_name == 'employee'):
        isSuccess = employee_save.upload(request)
        employee_data = Employee.objects.all() 
        return render(request, 'myApp/employee.html', { "isUpload" : isSuccess , "employee_data" : employee_data })
    # if(table_name == 'samsung_code'):
    #     samsung_code_save.upload(request)
    #     samsung_code_data = SamsungCode.objects.all() 
    #     return render(request, 'myApp/samsung_code.html', { "isUpload" : isSuccess , "samsung_code_data" : samsung_code_data })
    if(table_name == 'product'):
        isSuccess = product_save.upload(request)
        product_data = Product.objects.all()
        return render(request, 'myApp/product.html', { "isUpload" : isSuccess , "product_data" : product_data })
    # if(table_name == 'broker'):
    #     broker_save.upload(request)
    #     broker_data = Broker.objects.all()
    #     return render(request, 'myApp/broker.html', { "isUpload" : isSuccess , "broker_data" : broker_data }) 
    # if(table_name == 'customer'):
    #     customer_save.upload(request)
    #     customer_data = Customer.objects.all()
    #     return render(request, 'myApp/customer.html', { "isUpload" : isSuccess , "customer_data" : customer_data }) 

def select_table(request, table_name):
    if(table_name == 'employee'):
        employee_data = Employee.objects.all() 
        return render(request, 'myApp/employee.html', { "employee_data" : employee_data })
    if(table_name == 'samsung_code'):
        samsung_code_data = SamsungCode.objects.all() 
        return render(request, 'myApp/samsung_code.html', { "samsung_code_data" : samsung_code_data })
    if(table_name == 'authority'):
        authority_data = Authority.objects.all() 
        return render(request, 'myApp/authority_select.html', { "authority_data" : authority_data })
    if(table_name == 'product'):
        product_data = Product.objects.all()
        return render(request, 'myApp/product.html', { "product_data" : product_data })
    if(table_name == 'customer'):
        customer_data = Customer.objects.all()
        return render(request, 'myApp/customer_select.html', { "customer_data" : customer_data })
    if(table_name == 'customer_purchasing'):
        customer_purchasing_data = CustomerPurchasing.objects.all()
        return render(request, 'myApp/customer_purchasing_select.html', { "customer_purchasing_data" : customer_purchasing_data })
    if(table_name == 'customer_settlement'):
        customer_settlement_data = CustomerSettlement.objects.all()
        return render(request, 'myApp/customer_settlement_select.html', { "customer_settlement_data" : customer_settlement_data })
    if(table_name == 'co_salesman'):
        co_salesman_data = CoSalesman.objects.all()
        return render(request, 'myApp/co_salesman_select.html', { "co_salesman_data" : co_salesman_data })
    if(table_name == 'broker'):
        broker_data = Broker.objects.all()
        return render(request, 'myApp/broker_select.html', { "broker_data" : broker_data })
    if(table_name == 'sales'):
        sales_data = Sales.objects.all()
        return render(request, 'myApp/sales_select.html', { "sales_data" : sales_data })
    if(table_name == 'sales_content'):
        sales_content_data = SalesContent.objects.all()
        return render(request, 'myApp/sales_content_select.html', { "sales_content_data" : sales_content_data })
    if(table_name == 'approval'):
        approval_data = Approval.objects.all()
        return render(request, 'myApp/approval_select.html', { "approval_data" : approval_data })
    if(table_name == 'order'):
        order_data = OrderData.objects.all() 
        return render(request, 'myApp/order_select.html', { "order_data" : order_data })
    if(table_name == 'deposit'):
        deposit_data = Deposit.objects.all()
        return render(request, 'myApp/deposit_select.html', { "deposit_data" : deposit_data })
    if(table_name == 'delivery'):
        delivery_data = Delivery.objects.all()
        return render(request, 'myApp/delivery_select.html', { "delivery_data" : delivery_data })

def select(request):
    return render(request, 'myApp/select.html')

def select_result(request):
    print(request.POST.get('oppty_num'))
    data = scm_select.select(request)
    return render(request, 'myApp/select_result.html', { "data" : data })

def order_upload(request):
    if request.method == 'POST':
        if 'file' in request.FILES:
            wb = load_workbook(filename=request.FILES['file'].file)
            first_sheet = wb.get_sheet_names()[0]
            worksheet = wb.get_sheet_by_name(first_sheet)
            print(worksheet)
            
            for row in worksheet.iter_rows(min_row=2): # Offset for header
                order = OrderData()
                order.order_num = row[0].value
                order.sales_num = row[1].value
                order.product_model_name = row[2].value
                order.order_quantity = row[3].value
                order.order_date = row[4].value
                order.quote_num = row[5].value
                order.scheduled_delivery_date = row[6].value
                order.assignment = row[7].value
                order.recipient = row[8].value
                order.recipient_phone = row[9].value
                order.delivery_address = row[10].value
                order.balance = row[11].value
                order.order_close = row[12].value
                print(order.balance)

                if order.balance == None : 
                    # 입력이 안되었으면 자동으로 계산되도록 
                    # 수량 = 승인수량 - 주문수량
                    # balance = Approval.approval_quantity - order_quantity 
                    try :
                        row = Approval.objects.get(sales_num=order.sales_num)
                        if order.order_quantity != None and row.approval_quantity != None:  
                            order.balance = row.approval_quantity - order.order_quantity
                        elif row.approval_quantity != None and order.order_quantity == None:
                            order.balance = row.approval_quantity
                        else:
                            order.balance = None
                    except ObjectDoesNotExist:
                        print("예외")
                        order.balance = None
                
                if order.order_num != None:
                    order.save()

        order_data = OrderData.objects.all() 
        print(order_data)
        return render(request, 'myApp/order_result.html', { "order_data" : order_data })