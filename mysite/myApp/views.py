from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from openpyxl import load_workbook
from openpyxl import Workbook
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import login as auth_loginz
# from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login
from django.contrib.auth import logout 
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
import json
import datetime

from .models import Employee
from .models import SamsungCode
from .models import Product
from .models import Customer
from .models import Broker
from .models import Proposal
from .models import Approval
from .models import OrderData
from .models import Deposit
from .models import Delivery
from .models import Scm

from . import business_support_select

from . import employee_save
from . import samsung_code_save
from . import product_save
from . import customer_save
from . import broker_save
from . import delivery_save
from . import deposit_save
from . import order_save
from . import approval_save
from . import scm_select
from . import proposal_save
from . import settlement_save

from django.db import connection

# @login_required
def index(request):
    data = scm_select.select(request)
    return render(request, 'myApp/scm.html', { "data" : data })  

# @login_required
def select(request):
    data = scm_select.select(request)
    return render(request, 'myApp/scm.html', { "data" : data })

def select_result(request):
    print("select_result")
    data = scm_select.find(request)
    return render(request, 'myApp/scm.html', { "data" : data })

def sales_autocomplete(request):
    print("자동완성")
    sales_data = Employee.objects.filter(name__istartswith=request.GET['term'], charge="INNO 영업담당")
    print(sales_data)
    results = []
    for i in sales_data : 
        i_json = {}
        i_json['id'] = i.name
        i_json['label'] = i.name
        i_json['value'] = i.name
        results.append(i_json)
    data = json.dumps(results)
    mimetype = 'application/json'
    return HttpResponse(data,mimetype)

def scm_autocomplete(request):
    print("자동완성")
    scm_data = Employee.objects.filter(name__istartswith=request.GET['term'], charge="INNO SCM담당")
    print(scm_data)
    results = []
    for i in scm_data : 
        i_json = {}
        i_json['id'] = i.name
        i_json['label'] = i.name
        i_json['value'] = i.name
        results.append(i_json)
    data = json.dumps(results)
    mimetype = 'application/json'
    return HttpResponse(data,mimetype)

def samsung_code_autocomplete(request):
    print("자동완성")
    samsung_code_data = SamsungCode.objects.filter(samsung_code__istartswith=request.GET['term'])
    print(samsung_code_data)
    results = []
    for i in samsung_code_data : 
        i_json = {}
        i_json['id'] = i.samsung_code
        i_json['label'] = i.samsung_code
        i_json['value'] = i.samsung_code
        results.append(i_json)
    data = json.dumps(results)
    mimetype = 'application/json'
    return HttpResponse(data,mimetype)

def employee_autocomplete(request):
    print("자동완성")
    manager_data = Employee.objects.filter(name__istartswith=request.GET['term'])
    print(manager_data)
    results = []
    for i in manager_data : 
        i_json = {}
        i_json['id'] = i.name
        i_json['label'] = i.name
        i_json['value'] = i.name
        results.append(i_json)
    data = json.dumps(results)
    mimetype = 'application/json'
    return HttpResponse(data,mimetype)

def samsung_sales_manager_autocomplete(request):
    print("자동완성")
    samsung_sales_manager_data = SamsungCode.objects.filter(manager__istartswith=request.GET['term'])
    print(samsung_sales_manager_data)
    results = []
    for i in samsung_sales_manager_data : 
        i_json = {}
        i_json['id'] = i.manager
        i_json['label'] = i.manager
        i_json['value'] = i.manager
        results.append(i_json)
    data = json.dumps(results)
    mimetype = 'application/json'
    return HttpResponse(data,mimetype)

def broker_autocomplete(request):
    print("자동완성")
    sales_manager_data = Broker.objects.filter(name__istartswith=request.GET['term'])
    print(sales_manager_data)
    results = []
    for i in sales_manager_data : 
        i_json = {}
        i_json['id'] = i.name
        i_json['label'] = i.name
        i_json['value'] = i.name
        results.append(i_json)
    data = json.dumps(results)
    mimetype = 'application/json'
    return HttpResponse(data,mimetype)
    
def productno_autocomplete(request):
    print("자동완성")
    product_data = Product.objects.filter(productno__istartswith=request.GET['term'])
    print(product_data)
    results = []
    for i in product_data : 
        i_json = {}
        i_json['id'] = i.productno
        i_json['label'] = i.productno
        i_json['value'] = i.productno
        results.append(i_json)
    data = json.dumps(results)
    mimetype = 'application/json'
    return HttpResponse(data,mimetype)

def customer_name_autocomplete(request):
    print("자동완성")
    customer_name_data = Customer.objects.filter(customer_name__istartswith=request.GET['term'])
    print(customer_name_data)
    results = []
    for i in customer_name_data : 
        i_json = {}
        i_json['id'] = i.customer_name
        i_json['label'] = i.customer_name + " 사업자등록번호:" + i.company_registration_number 
        i_json['value'] = i.customer_name + " 사업자등록번호:" + i.company_registration_number 
        results.append(i_json)
    data = json.dumps(results)
    mimetype = 'application/json'
    return HttpResponse(data,mimetype)

def customer_name_autocomplete_oppty_num(request):
    # approval에서 사용
    print("자동완성")
    customer_name_data = Proposal.objects.filter(customer_name__istartswith=request.GET['term'])
    # print(customer_name_data)
    results = []
    for i in customer_name_data : 
        i_json = {}
        i_json['id'] = i.customer_name
        i_json['label'] = i.customer_name + " oppty_num:" + i.oppty_num 
        i_json['value'] = i.customer_name + " oppty_num:" + i.oppty_num 
        if i_json not in results:
            results.append(i_json)
    # print(results)
    data = json.dumps(results)
    mimetype = 'application/json'
    return HttpResponse(data,mimetype)

# @login_required
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
    if(table_name == 'proposal'):
        return render(request, 'myApp/proposal.html', )  
    if(table_name == 'approval'):
        approval_data = Approval.objects.raw('SELECT approval. *,  proposal.buy_place, proposal.decision_quantity,  proposal.delivery_request_date  FROM  approval INNER JOIN proposal ON approval.oppty_num = proposal.oppty_num AND approval.productno = proposal.productno AND approval.recipient = proposal.recipient ;')
        return render(request, 'myApp/approval.html', { "approval_data" : approval_data })   
    if(table_name == 'order'):
        order_data = OrderData.objects.raw('SELECT * FROM ( SELECT approval. *,  proposal.sales_unit, proposal.sales_price, proposal.delivery_address, proposal.recipient_phone1, proposal.recipient_phone2, proposal.buy_place, proposal.decision_quantity,  proposal.delivery_request_date  FROM  approval INNER JOIN proposal ON approval.oppty_num = proposal.oppty_num AND approval.productno = proposal.productno AND approval.recipient = proposal.recipient ) temp inner JOIN order_data ON temp.productno=order_data.productno AND temp.oppty_num=order_data.oppty_num AND temp.recipient=order_data.recipient AND temp.quote_num=order_data.quote_num;')
        return render(request, 'myApp/order.html', { "order_data" : order_data }) 
    if(table_name == 'deposit'):
        deposit_data = Deposit.objects.all()
        return render(request, 'myApp/deposit.html', { "deposit_data" : deposit_data }) 
    if(table_name == 'delivery'):
        # all_data = OrderData.objects.raw('SELECT * FROM order_data INNER JOIN approval ON order_data.oppty_num=approval.oppty_num AND order_data.quote_num=approval.quote_num AND order_data.recipient=approval.recipient AND order_data.productno=approval.productno INNER JOIN (SELECT proposal.*, deposit.deposit_balance FROM proposal INNER JOIN deposit ON proposal.customer_name=deposit.customer_name AND proposal.company_registration_number=deposit.company_registration_number) proposal_deposit ON order_data.oppty_num=proposal_deposit.oppty_num AND order_data.recipient=proposal_deposit.recipient AND order_data.productno=proposal_deposit.productno INNER JOIN delivery ON order_data.order_num=delivery.order_num; ')
        all_data = OrderData.objects.raw('SELECT * FROM order_data  INNER JOIN approval ON order_data.oppty_num=approval.oppty_num AND order_data.quote_num=approval.quote_num AND order_data.recipient=approval.recipient AND order_data.productno=approval.productno  INNER JOIN (SELECT proposal.*, customer_deposit_balance.deposit_balance FROM proposal INNER JOIN customer_deposit_balance ON proposal.company_registration_number=customer_deposit_balance.company_registration_number) proposal_deposit ON order_data.oppty_num=proposal_deposit.oppty_num AND order_data.recipient=proposal_deposit.recipient AND order_data.productno=proposal_deposit.productno INNER JOIN delivery ON order_data.order_num=delivery.order_num;')
        return render(request, 'myApp/delivery.html', { "all_data" : all_data }) 
    if(table_name == 'settlement'):
        all_data = OrderData.objects.raw('SELECT * FROM order_data  INNER JOIN approval ON order_data.oppty_num=approval.oppty_num AND order_data.quote_num=approval.quote_num AND order_data.recipient=approval.recipient AND order_data.productno=approval.productno  INNER JOIN (SELECT proposal.*, customer_deposit_balance.deposit_balance FROM proposal INNER JOIN customer_deposit_balance ON proposal.company_registration_number=customer_deposit_balance.company_registration_number) proposal_deposit ON order_data.oppty_num=proposal_deposit.oppty_num AND order_data.recipient=proposal_deposit.recipient AND order_data.productno=proposal_deposit.productno INNER JOIN delivery ON order_data.order_num=delivery.order_num inner join settlement ON order_data.order_num=settlement.order_num AND order_data.quote_num=settlement.quote_num AND  order_data.oppty_num=settlement.oppty_num AND order_data.productno=settlement.productno AND order_data.recipient=settlement.recipient;')
        return render(request, 'myApp/settlement.html', { "all_data" : all_data }) 
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

# @login_required
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
        return render(request, 'myApp/broker.html', { "isSave" : isSuccess , "broker_data" : broker_data }) 
    if(table_name == 'customer'):
        isSuccess = customer_save.save(request)
        customer_data = Customer.objects.all()
        return render(request, 'myApp/customer.html', { "isSave" : isSuccess , "customer_data" : customer_data })   
    if(table_name == 'proposal'):
        isSuccess = proposal_save.save(request)
        print(isSuccess)
        if isSuccess == "중개사 등록 필요":
            broker_data = Broker.objects.all()
            return render(request, 'myApp/broker.html', { "isSave" : isSuccess , "broker_data" : broker_data }) 
        elif isSuccess == "업체 등록 필요":
            customer_data = Customer.objects.all()
            return render(request, 'myApp/customer.html', { "isSave" : isSuccess , "customer_data" : customer_data })  
        return render(request, 'myApp/proposal.html',  { "isSave" : isSuccess })  
    if(table_name == 'approval'):
        isSuccess = approval_save.save(request)
        approval_data = Approval.objects.raw('SELECT approval. *,  proposal.buy_place, proposal.decision_quantity,  proposal.delivery_request_date  FROM  approval INNER JOIN proposal ON approval.oppty_num = proposal.oppty_num AND approval.productno = proposal.productno AND approval.recipient = proposal.recipient ;')    
        return render(request, 'myApp/approval.html', { "isSave" : isSuccess , "approval_data" : approval_data })   
    if(table_name == 'order'):
        isSuccess = order_save.save(request)
        order_data = OrderData.objects.raw('SELECT * FROM ( SELECT approval. *,  proposal.sales_unit, proposal.sales_price, proposal.delivery_address, proposal.recipient_phone1, proposal.recipient_phone2, proposal.buy_place, proposal.decision_quantity,  proposal.delivery_request_date  FROM  approval INNER JOIN proposal ON approval.oppty_num = proposal.oppty_num AND approval.productno = proposal.productno AND approval.recipient = proposal.recipient ) temp inner JOIN order_data ON temp.productno=order_data.productno AND temp.oppty_num=order_data.oppty_num AND temp.recipient=order_data.recipient AND temp.quote_num=order_data.quote_num;')
        return render(request, 'myApp/order.html', { "isSave" : isSuccess, "order_data" : order_data })
    if(table_name == 'deposit'):
        deposit_data = Deposit.objects.all()
        isSuccess = deposit_save.save(request)
        return render(request, 'myApp/deposit.html', { "isSave" : isSuccess , "deposit_data" : deposit_data })
    if(table_name == 'delivery'):
        isSuccess = delivery_save.save(request)
        all_data = OrderData.objects.raw('SELECT * FROM order_data  INNER JOIN approval ON order_data.oppty_num=approval.oppty_num AND order_data.quote_num=approval.quote_num AND order_data.recipient=approval.recipient AND order_data.productno=approval.productno  INNER JOIN (SELECT proposal.*, customer_deposit_balance.deposit_balance FROM proposal INNER JOIN customer_deposit_balance ON proposal.company_registration_number=customer_deposit_balance.company_registration_number) proposal_deposit ON order_data.oppty_num=proposal_deposit.oppty_num AND order_data.recipient=proposal_deposit.recipient AND order_data.productno=proposal_deposit.productno INNER JOIN delivery ON order_data.order_num=delivery.order_num;')
        return render(request, 'myApp/delivery.html', { "isSave" : isSuccess, "all_data" : all_data })
    if(table_name == 'settlement'):
        isSuccess = settlement_save.save(request)
        all_data = OrderData.objects.raw('SELECT * FROM order_data  INNER JOIN approval ON order_data.oppty_num=approval.oppty_num AND order_data.quote_num=approval.quote_num AND order_data.recipient=approval.recipient AND order_data.productno=approval.productno  INNER JOIN (SELECT proposal.*, customer_deposit_balance.deposit_balance FROM proposal INNER JOIN customer_deposit_balance ON proposal.company_registration_number=customer_deposit_balance.company_registration_number) proposal_deposit ON order_data.oppty_num=proposal_deposit.oppty_num AND order_data.recipient=proposal_deposit.recipient AND order_data.productno=proposal_deposit.productno INNER JOIN delivery ON order_data.order_num=delivery.order_num inner join settlement ON order_data.order_num=settlement.order_num AND order_data.quote_num=settlement.quote_num AND  order_data.oppty_num=settlement.oppty_num AND order_data.productno=settlement.productno AND order_data.recipient=settlement.recipient;')
        return render(request, 'myApp/settlement.html', { "isSave" : isSuccess, "all_data" : all_data })
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
    # if(table_name == 'approval'):
    #     try: 
    #         approval_save.save(request)
    #         return render(request, 'myApp/approval_insert.html', { "isSave" : True })
    #     except IntegrityError as e:
    #         return render(request, 'myApp/approval_insert.html', { "isIntegrity" : True })
    # if(table_name == 'order'):
    #     try: 
    #         order_save.save(request)
    #         return render(request, 'myApp/order_insert.html', { "isSave" : True })
    #     except IntegrityError as e:
    # #         return render(request, 'myApp/order_insert.html', { "isIntegrity" : True })
    # if(table_name == 'deposit'):
    #     try: 
    #         deposit_save.save(request)
    #         return render(request, 'myApp/deposit_insert.html', { "isSave" : True })
    #     except IntegrityError as e:
    #         return render(request, 'myApp/deposit_insert.html', { "isIntegrity" : True })
    # if(table_name == 'delivery'):
    #     try: 
    #         delivery_save.save(request)
    #         return render(request, 'myApp/delivery_insert.html', { "isSave" : True })
    #     except IntegrityError as e:
    #         return render(request, 'myApp/delivery_insert.html', { "isIntegrity" : True })

# @login_required
def upload(request, table_name):
    print(table_name)
    if(table_name == 'employee'):
        isSuccess = employee_save.upload(request)
        employee_data = Employee.objects.all() 
        return render(request, 'myApp/employee.html', { "isUpload" : isSuccess , "employee_data" : employee_data })
    if(table_name == 'samsung_code'):
        isSuccess = samsung_code_save.upload(request)
        samsung_code_data = SamsungCode.objects.all() 
        return render(request, 'myApp/samsung_code.html', { "isUpload" : isSuccess , "samsung_code_data" : samsung_code_data })
    if(table_name == 'product'):
        isSuccess = product_save.upload(request)
        product_data = Product.objects.all()
        return render(request, 'myApp/product.html', { "isUpload" : isSuccess , "product_data" : product_data })
    if(table_name == 'broker'):
        isSuccess = broker_save.upload(request)
        broker_data = Broker.objects.all()
        return render(request, 'myApp/broker.html', { "isUpload" : isSuccess , "broker_data" : broker_data }) 
    if(table_name == 'customer'):
        isSuccess = customer_save.upload(request)
        customer_data = Customer.objects.all()
        return render(request, 'myApp/customer.html', { "isUpload" : isSuccess , "customer_data" : customer_data })   

# @login_required
def download(request, table_name):
    print(table_name)
    if(table_name == 'employee'):
        isSuccess = employee_save.download(request)
        employee_data = Employee.objects.all() 
        return render(request, 'myApp/employee.html', { "isDownload" : isSuccess , "employee_data" : employee_data })
    if(table_name == 'samsung_code'):
        samsung_code_save.upload(request)
        samsung_code_data = SamsungCode.objects.all() 
        return render(request, 'myApp/samsung_code.html', { "isDownload" : isSuccess , "samsung_code_data" : samsung_code_data })
    if(table_name == 'product'):
        isSuccess = product_save.download(request)
        product_data = Product.objects.all()
        return render(request, 'myApp/product.html', { "isDownload" : isSuccess , "product_data" : product_data })
    if(table_name == 'broker'):
        isSuccess = broker_save.download(request)
        broker_data = Broker.objects.all()
        return render(request, 'myApp/broker.html', { "error" : isSuccess , "broker_data" : broker_data }) 
    if(table_name == 'customer'):
        isSuccess = customer_save.download(request)
        customer_data = Customer.objects.all()
        return render(request, 'myApp/customer.html', { "error" : isSuccess , "customer_data" : customer_data })
    if(table_name == 'scm'):
        isSuccess = scm_select.download(request)
        data = scm_select.find(request)
        return render(request, 'myApp/scm.html', { "error" : isSuccess , "data" : data }) 

def select_proposal(request):
    select_oppty_num = proposal_save.select(request)
    proposal_data = Proposal.objects.filter(oppty_num=select_oppty_num).first()
    return render(request, 'myApp/proposal.html', { "select_oppty_num" : select_oppty_num, "proposal_data" : proposal_data })

def modify_proposal(request):
    isSuccess = proposal_save.modify(request)
    if isSuccess == "중개사 등록 필요":
        broker_data = Broker.objects.all()
        return render(request, 'myApp/broker.html', { "isSave" : isSuccess , "broker_data" : broker_data }) 
    elif isSuccess == "업체 등록 필요":
        customer_data = Customer.objects.all()
        return render(request, 'myApp/customer.html', { "isSave" : isSuccess , "customer_data" : customer_data })  
    proposal_data = Proposal.objects.all()
    return render(request, 'myApp/proposal.html',  { "isSave" : isSuccess , "proposal_data" : proposal_data })  

# def select_table(request, table_name):
#     if(table_name == 'employee'):
#         employee_data = Employee.objects.all() 
#         return render(request, 'myApp/employee.html', { "employee_data" : employee_data })
#     if(table_name == 'samsung_code'):
#         samsung_code_data = SamsungCode.objects.all() 
#         return render(request, 'myApp/samsung_code.html', { "samsung_code_data" : samsung_code_data })
#     if(table_name == 'authority'):
#         authority_data = Authority.objects.all() 
#         return render(request, 'myApp/authority_select.html', { "authority_data" : authority_data })
#     if(table_name == 'product'):
#         product_data = Product.objects.all()
#         return render(request, 'myApp/product.html', { "product_data" : product_data })
#     if(table_name == 'customer'):
#         customer_data = Customer.objects.all()
#         return render(request, 'myApp/customer_select.html', { "customer_data" : customer_data })
#     if(table_name == 'customer_purchasing'):
#         customer_purchasing_data = CustomerPurchasing.objects.all()
#         return render(request, 'myApp/customer_purchasing_select.html', { "customer_purchasing_data" : customer_purchasing_data })
#     if(table_name == 'customer_settlement'):
#         customer_settlement_data = CustomerSettlement.objects.all()
#         return render(request, 'myApp/customer_settlement_select.html', { "customer_settlement_data" : customer_settlement_data })
#     if(table_name == 'co_salesman'):
#         co_salesman_data = CoSalesman.objects.all()
#         return render(request, 'myApp/co_salesman_select.html', { "co_salesman_data" : co_salesman_data })
#     if(table_name == 'broker'):
#         broker_data = Broker.objects.all()
#         return render(request, 'myApp/broker_select.html', { "broker_data" : broker_data })
#     if(table_name == 'sales'):
#         sales_data = Sales.objects.all()
#         return render(request, 'myApp/sales_select.html', { "sales_data" : sales_data })
#     if(table_name == 'sales_content'):
#         sales_content_data = SalesContent.objects.all()
#         return render(request, 'myApp/sales_content_select.html', { "sales_content_data" : sales_content_data })
#     if(table_name == 'approval'):
#         approval_data = Approval.objects.all()
#         return render(request, 'myApp/approval_select.html', { "approval_data" : approval_data })
#     if(table_name == 'order'):
#         order_data = OrderData.objects.all() 
#         return render(request, 'myApp/order_select.html', { "order_data" : order_data })
#     if(table_name == 'deposit'):
#         deposit_data = Deposit.objects.all()
#         return render(request, 'myApp/deposit_select.html', { "deposit_data" : deposit_data })
#     if(table_name == 'delivery'):
#         delivery_data = Delivery.objects.all()
#         return render(request, 'myApp/delivery_select.html', { "delivery_data" : delivery_data })

# def order_upload(request):
#     if request.method == 'POST':
#         if 'file' in request.FILES:
#             wb = load_workbook(filename=request.FILES['file'].file)
#             first_sheet = wb.get_sheet_names()[0]
#             worksheet = wb.get_sheet_by_name(first_sheet)
#             print(worksheet)
            
#             for row in worksheet.iter_rows(min_row=2): # Offset for header
#                 order = OrderData()
#                 order.order_num = row[0].value
#                 order.sales_num = row[1].value
#                 order.product_model_name = row[2].value
#                 order.order_quantity = row[3].value
#                 order.order_date = row[4].value
#                 order.quote_num = row[5].value
#                 order.scheduled_delivery_date = row[6].value
#                 order.assignment = row[7].value
#                 order.recipient = row[8].value
#                 order.recipient_phone = row[9].value
#                 order.delivery_address = row[10].value
#                 order.balance = row[11].value
#                 order.order_close = row[12].value
#                 print(order.balance)

#                 if order.balance == None : 
#                     # 입력이 안되었으면 자동으로 계산되도록 
#                     # 수량 = 승인수량 - 주문수량
#                     # balance = Approval.approval_quantity - order_quantity 
#                     try :
#                         row = Approval.objects.get(sales_num=order.sales_num)
#                         if order.order_quantity != None and row.approval_quantity != None:  
#                             order.balance = row.approval_quantity - order.order_quantity
#                         elif row.approval_quantity != None and order.order_quantity == None:
#                             order.balance = row.approval_quantity
#                         else:
#                             order.balance = None
#                     except ObjectDoesNotExist: 
#                         print("예외")
#                         order.balance = None
                
#                 if order.order_num != None:
#                     order.save()

#         order_data = OrderData.objects.all() 
#         print(order_data)
#         return render(request, 'myApp/order_result.html', { "order_data" : order_data })

def signin(request):
    print("로그인")
    form = AuthenticationForm()
    try:
        if request.method == 'POST':
            user_id = request.POST.get('username',None)
            print(user_id)
            password = request.POST.get('password',None)
            print(password)
            # user = User.objects.get(username=user_id)
            # print(user)
            # print(user.username)
            # print(user.password)
            # user.first_name=user_id
            # user.set_password(password) # 비밀번호 변경 함수
            # user.save()
            user_id = request.POST.get('username',None)
            password = request.POST.get('password',None)
            login_user = authenticate(username=user_id, password=password)
            if login_user is not None:
                print(login_user)
                login(request, login_user)
                print("성공")
                return render(request,"myApp/main.html")
            else:
                error = '아이디나 비밀번호가 일치하지 않습니다.'
                print('User not found')
                return render(request, 'myApp/login.html', {'form': form, 'error': error})
        else:
            return render(request, 'myApp/login.html', {'form': form })
    except:
        error = '아이디나 비밀번호가 일치하지 않습니다.'
        print("error")
        return render(request, 'myApp/login.html', {'form': form, 'error': error})

# @login_required
def signout(request):
    logout(request)
    return signin(request)

def get_propoal_data_from_oppty(request):
    # approval.html에서 사용
    # oppty넘버를 통해서 Proposal에 등록된 정보를 가져옴 
    # select_oppty_num
    approval_data = Approval.objects.raw('SELECT approval. *,  proposal.buy_place, proposal.decision_quantity,  proposal.delivery_request_date  FROM  approval INNER JOIN proposal ON approval.oppty_num = proposal.oppty_num AND approval.productno = proposal.productno AND approval.recipient = proposal.recipient ;')    
    select_oppty_num = request.POST.get('select_oppty_num',None)
    select_customer_name = request.POST.get('select_customer_name',None)
    print(select_oppty_num)
    
    isCustomerRight = Customer.objects.filter(customer_name=select_customer_name).count()

    try:
        if isCustomerRight != 0:
            proposal_data = Proposal.objects.filter(oppty_num=select_oppty_num)
            print(proposal_data)
            return render(request, 'myApp/approval.html', {"select_customer_name" : select_customer_name, "select_oppty_num" : select_oppty_num, 'proposal_data': proposal_data, "approval_data" : approval_data })   
        else:
            return render(request, 'myApp/approval.html', {'error' : "oppty번호나 업체명이 유효하지 않습니다.", "approval_data" : approval_data })   
    except:
        return render(request, 'myApp/approval.html', {'error' : "oppty번호나 업체명이 유효하지 않습니다.", "approval_data" : approval_data })   

def get_approval_data_from_select_quote_num(request):
    # order.html에서 사용
    # elect_quote_num를 통해서 Approval 등록된 정보를 가져옴 
    # select_quote_num
    # approval_data = Approval.objects.all()
    select_quote_num = request.POST.get('select_quote_num',None)
    print(select_quote_num)
    
    optty_num = request.POST.get('optty_num',None)
    print(optty_num)

    order_data = OrderData.objects.raw('SELECT * FROM ( SELECT approval. *,  proposal.sales_unit, proposal.sales_price, proposal.delivery_address, proposal.recipient_phone1, proposal.recipient_phone2, proposal.buy_place, proposal.decision_quantity,  proposal.delivery_request_date  FROM  approval INNER JOIN proposal ON approval.oppty_num = proposal.oppty_num AND approval.productno = proposal.productno AND approval.recipient = proposal.recipient ) temp inner JOIN order_data ON temp.productno=order_data.productno AND temp.oppty_num=order_data.oppty_num AND temp.recipient=order_data.recipient AND temp.quote_num=order_data.quote_num;')
    isQuoteNumRight = Approval.objects.filter(quote_num=select_quote_num).count()

    try:
        if isQuoteNumRight != 0:
            approval_data = Approval.objects.filter(quote_num=select_quote_num)
            print(approval_data)
            print(approval_data.first().oppty_num)
            return render(request, 'myApp/order.html', {"select_quote_num" : select_quote_num, "approval_data" : approval_data, "order_data" : order_data })  
        else:
            return render(request, 'myApp/order.html', {'error' : "견적번호가 유효하지 않습니다.", "order_data" : order_data })   
    except:
        return render(request, 'myApp/order.html', {'error' : "견적번호가 유효하지 않습니다.", "order_data" : order_data })   

def get_deposit_data_from_company_registration_number(request):
    # deposit.html에서 사용
    # company_registration_number 통해서 deposit 등록된 정보를 가져옴 

    company_registration_number = request.POST.get('select_company_registration_number',None)
    print(company_registration_number)

    isCompany_registration_numberRight = Deposit.objects.filter(company_registration_number=company_registration_number).count()

    try:
        if isQuoteNumRight != 0:
            approval_data = Approval.objects.filter(quote_num=select_quote_num)
            print(approval_data)
            print(approval_data.first().oppty_num)
            return render(request, 'myApp/order.html', {"select_quote_num" : select_quote_num, "approval_data" : approval_data, "order_data" : order_data })  
        else:
            return render(request, 'myApp/order.html', {'error' : "사업자등록번호가 유효하지 않습니다.", "order_data" : order_data })   
    except:
        return render(request, 'myApp/order.html', {'error' : "사업자등록번호가 유효하지 않습니다.", "order_data" : order_data })   

def get_data_from_select_scheduled_delivery_date(request):
    # delivery.html에서 사용
    # select_scheduled_delivery_date 통해서 등록된 정보를 가져옴 

    scheduled_delivery_date = request.POST.get('select_scheduled_delivery_date',None)
    print(scheduled_delivery_date)

    isScheduled_delivery_dateRight = OrderData.objects.filter(scheduled_delivery_date=scheduled_delivery_date).count()
    print(isScheduled_delivery_dateRight)
    data = OrderData.objects.raw('SELECT * FROM order_data INNER JOIN approval ON order_data.oppty_num=approval.oppty_num AND order_data.quote_num=approval.quote_num AND order_data.recipient=approval.recipient AND order_data.productno=approval.productno INNER JOIN (SELECT proposal.*, customer_deposit_balance.deposit_balance FROM proposal INNER JOIN customer_deposit_balance ON proposal.company_registration_number=customer_deposit_balance.company_registration_number) proposal_deposit ON order_data.oppty_num=proposal_deposit.oppty_num AND order_data.recipient=proposal_deposit.recipient AND order_data.productno=proposal_deposit.productno;')
    all_data = OrderData.objects.raw('SELECT * FROM order_data  INNER JOIN approval ON order_data.oppty_num=approval.oppty_num AND order_data.quote_num=approval.quote_num AND order_data.recipient=approval.recipient AND order_data.productno=approval.productno  INNER JOIN (SELECT proposal.*, customer_deposit_balance.deposit_balance FROM proposal INNER JOIN customer_deposit_balance ON proposal.company_registration_number=customer_deposit_balance.company_registration_number) proposal_deposit ON order_data.oppty_num=proposal_deposit.oppty_num AND order_data.recipient=proposal_deposit.recipient AND order_data.productno=proposal_deposit.productno INNER JOIN delivery ON order_data.order_num=delivery.order_num;')
    try:
        if isScheduled_delivery_dateRight != 0:
            # data = data.filter(scheduled_delivery_date=scheduled_delivery_date)
            result_data = []
            for i in data :
                print(i.scheduled_delivery_date)
                if i.scheduled_delivery_date.strftime('%Y-%m-%d') == scheduled_delivery_date:
                    result_data.append(i)
                    print(i.deposit_balance)
            print(result_data)
            return render(request, 'myApp/delivery.html', {"select_scheduled_delivery_date" : scheduled_delivery_date, "data" : result_data, "all_data" : all_data })  
        else:
            return render(request, 'myApp/delivery.html', {'error' : "납품예정일이 유효하지 않습니다.", "all_data" : all_data })  
    except:
        return render(request, 'myApp/delivery.html', {'error' : "납품예정일이 유효하지 않습니다.", "all_data" : all_data })  

def get_data_from_delivery_date(request):
    select_delivery_date_start = request.POST.get('select_delivery_date_start',0)
    select_delivery_date_end = request.POST.get('select_delivery_date_end',0)
    select_customer_name = request.POST.get('select_customer_name',0)
    print(select_customer_name)
    all_data = OrderData.objects.raw('SELECT * FROM order_data  INNER JOIN approval ON order_data.oppty_num=approval.oppty_num AND order_data.quote_num=approval.quote_num AND order_data.recipient=approval.recipient AND order_data.productno=approval.productno  INNER JOIN (SELECT proposal.*, customer_deposit_balance.deposit_balance FROM proposal INNER JOIN customer_deposit_balance ON proposal.company_registration_number=customer_deposit_balance.company_registration_number) proposal_deposit ON order_data.oppty_num=proposal_deposit.oppty_num AND order_data.recipient=proposal_deposit.recipient AND order_data.productno=proposal_deposit.productno INNER JOIN delivery ON order_data.order_num=delivery.order_num inner join settlement ON order_data.order_num=settlement.order_num AND order_data.quote_num=settlement.quote_num AND  order_data.oppty_num=settlement.oppty_num AND order_data.productno=settlement.productno AND order_data.recipient=settlement.recipient;')
    selected_data = OrderData.objects.raw('SELECT * FROM order_data  INNER JOIN approval ON order_data.oppty_num=approval.oppty_num AND order_data.quote_num=approval.quote_num AND order_data.recipient=approval.recipient AND order_data.productno=approval.productno  INNER JOIN (SELECT proposal.*, customer_deposit_balance.deposit_balance FROM proposal INNER JOIN customer_deposit_balance ON proposal.company_registration_number=customer_deposit_balance.company_registration_number) proposal_deposit ON order_data.oppty_num=proposal_deposit.oppty_num AND order_data.recipient=proposal_deposit.recipient AND order_data.productno=proposal_deposit.productno INNER JOIN delivery ON order_data.order_num=delivery.order_num;')
    result_data = []
    for i in selected_data:
        if i.delivery_date.strftime('%Y-%m-%d') >= select_delivery_date_start and i.delivery_date.strftime('%Y-%m-%d') <= select_delivery_date_end: 
            if select_customer_name == '' or select_customer_name==None :
                result_data.append(i)
            else:
                if i.customer_name == select_customer_name:
                    result_data.append(i)

    return render(request, 'myApp/settlement.html', {'error' : "납품완료일에 해당하는 정보가 없습니다.", "select_delivery_date_start":select_delivery_date_start, "select_delivery_date_end" : select_delivery_date_end, "all_data":all_data, "result_data" : result_data})  

def business_support(request):
    data = scm_select.select(request)
    # data = business_support_select.find(request)
    return render(request, 'myApp/business_support.html', {"data" : data})  

def business_support_select(request):
    result_data = business_support_select.find(request)
    return render(request, 'myApp/business_support.html', {"data" : data})  
