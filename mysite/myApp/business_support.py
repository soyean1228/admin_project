from .models import Approval
from .models import OrderData
from .models import Deposit
from .models import Delivery
from .models import Scm
from openpyxl import load_workbook
from openpyxl import Workbook
import openpyxl
import datetime

def select(request):

    queryset = Scm.objects.all()
    queryset.delete() # 일괄 delete 요청    
    rawdata = Approval.objects.raw('SELECT tmp3.*, settlement.billing_date, settlement.billing_amount FROM ( SELECT tmp2.*, delivery.in_date, delivery.in_amount, delivery.delivery_date FROM ( SELECT tmp1.*,order_data.order_num, order_data.order_date, order_data.order_quantity, order_data.assignment, order_data.scheduled_delivery_date FROM ( SELECT proposal.*, approval.approval_quantity, approval.quote_num, approval.approval_unit, approval.approval_price FROM proposal LEFT JOIN approval ON proposal.oppty_num=approval.oppty_num AND proposal.productno=approval.productno AND proposal.recipient=approval.recipient) tmp1 LEFT JOIN order_data ON tmp1.oppty_num=order_data.oppty_num AND tmp1.productno=order_data.productno AND tmp1.recipient=order_data.recipient AND tmp1.quote_num=order_data.quote_num ) tmp2 LEFT JOIN delivery ON delivery.order_num=tmp2.order_num AND delivery.company_registration_number=tmp2.company_registration_number) tmp3 LEFT JOIN settlement ON settlement.order_num=tmp3.order_num AND settlement.quote_num=tmp3.quote_num AND settlement.oppty_num=tmp3.oppty_num AND settlement.productno=tmp3.productno AND settlement.recipient=tmp3.recipient;')
    
    for i in rawdata:
        scm = Scm()
        scm.scm_num = Scm.get_num(scm) + 1 
        print(scm.scm_num)
        scm.customer_name = i.customer_name
        scm.oppty_num = i.oppty_num
        scm.quote_num = i.quote_num
        scm.order_date = i.order_date
        scm.order_num = i.order_num
        scm.recipient = i.recipient
        scm.delivery_address = i.delivery_address
        scm.recipient_phone1 = i.recipient_phone1
        scm.recipient_phone2 = i.recipient_phone2
        scm.productno = i.productno
        scm.buy_place = i.buy_place
        scm.decision_quantity = i.decision_quantity
        scm.decision_unit = i.decision_unit
        scm.decision_price = i.decision_price
        scm.approval_unit = i.approval_unit
        scm.approval_price = i.approval_price
        scm.sales_unit = i.sales_unit
        scm.sales_price = i.sales_price
        scm.assignment = i.assignment
        scm.delivery_request_date = i.delivery_request_date
        scm.scheduled_delivery_date = i.scheduled_delivery_date
        scm.delivery_date = i.delivery_date
        scm.in_date = i.in_date
        scm.in_amount = i.in_amount
        scm.billing_place = i.billing_place
        scm.billing_date = i.billing_date
        scm.billing_amount = i.billing_amount
        scm.contact_conclusion_date = i.contact_conclusion_date
        scm.samsung_code = i.samsung_code
        scm.samsung_sales_manager = i.samsung_sales_manager
        scm.team = i.team
        scm.sales_manager = i.sales_manager
        scm.broker = i.broker
        scm.scm_manager = i.scm_manager
        scm.company_registration_number = i.company_registration_number
        scm.payment_method = i.payment_method
        scm.sales_type = i.sales_type
        scm.demand = i.demand
        scm.approval_quantity = i.approval_quantity
        scm.order_quantity = i.order_quantity
        scm.save()

    data = Scm.objects.all()
    print(data)
    for i in data:
        if i.order_num:
            i.decision_quantity = i.order_quantity
        elif i.quote_num:
            i.decision_quantity = i.approval_quantity
        i.save()
    
    return data

def find(request):

    data = Scm.objects.all()

    samsung_code = request.POST.get('samsung_code',0)
    if samsung_code != '':
        data = data.filter(samsung_code=samsung_code)
    samsung_sales_manager = request.POST.get('samsung_sales_manager',0)
    if samsung_sales_manager != '':
        data = data.filter(samsung_sales_manager=samsung_sales_manager)
    sales_manager = request.POST.get('sales_manager',0)
    if sales_manager != '':
        data = data.filter(sales_manager=sales_manager)
    scm_manager = request.POST.get('scm_manager',0)
    if scm_manager != '':
        data = data.filter(scm_manager=scm_manager)

    oppty_num = request.POST.get('oppty_num',0)
    if oppty_num != '':
        data = data.filter(oppty_num=oppty_num)
    quote_num = request.POST.get('quote_num',0)
    if quote_num != '':
        data = data.filter(quote_num=quote_num)
    order_num = request.POST.get('order_num',0)
    if order_num != '':
        data = data.filter(order_num=order_num)

    customer_name = request.POST.get('customer_name',0)
    if customer_name != '':
        data = data.filter(customer_name=customer_name)
    billing_place = request.POST.get('billing_place',0)
    if billing_place != '':
        data = data.filter(billing_place=billing_place)
    recipient = request.POST.get('recipient',0)
    if recipient != '':
        data = data.filter(recipient=recipient)
    delivery_address = request.POST.get('delivery_address',0)
    if delivery_address != '':
        data = data.filter(delivery_address=delivery_address)
    recipient_phone1 = request.POST.get('recipient_phone1',0)
    if recipient_phone1 != '':
        data = data.filter(recipient_phone1=recipient_phone1)

    order_date_start = request.POST.get('order_date_start','')
    order_date_end = request.POST.get('order_date_end','')

    delivery_request_date_start = request.POST.get('delivery_request_date_start',0)
    delivery_request_date_end = request.POST.get('delivery_request_date_end',0)

    scheduled_delivery_date_start = request.POST.get('scheduled_delivery_date_start' ,'')
    scheduled_delivery_date_end = request.POST.get('scheduled_delivery_date_end' ,'')

    delivery_date_start = request.POST.get('delivery_date_start',0)
    delivery_date_end = request.POST.get('delivery_date_end',0)
    
    result_data = []
    isInsert = 0
    for i in data :
        isInsert = 1
        if order_date_start != '' and order_date_end != '' :
            if i.order_date == None :
                isInsert = 0
            elif i.order_date.strftime('%Y-%m-%d') < order_date_start or i.order_date.strftime('%Y-%m-%d') > order_date_end: 
                isInsert = 0
        if delivery_request_date_start != '' and delivery_request_date_end != '':
            if i.delivery_request_date == None :
                isInsert = 0
            elif i.delivery_request_date.strftime('%Y-%m-%d') < delivery_request_date_start or i.delivery_request_date.strftime('%Y-%m-%d') > delivery_request_date_end: 
                isInsert = 0
        if scheduled_delivery_date_start != '' and scheduled_delivery_date_end != '':
            if i.scheduled_delivery_date == None :
                isInsert = 0
            elif i.scheduled_delivery_date.strftime('%Y-%m-%d') < scheduled_delivery_date_start or i.scheduled_delivery_date.strftime('%Y-%m-%d') > scheduled_delivery_date_end: 
                isInsert = 0
        if delivery_date_start != '' and delivery_date_end != '':
            if i.delivery_date == None :
                isInsert = 0
            elif i.delivery_date.strftime('%Y-%m-%d') < delivery_date_start or i.delivery_date.strftime('%Y-%m-%d') > delivery_date_end: 
                isInsert = 0
        if isInsert == 1:
            result_data.append(i)

    return result_data
