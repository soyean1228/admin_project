from .models import Approval
from .models import OrderData
from .models import Deposit
from .models import Delivery
from .models import Scm
from .models import BusinessSupport
from openpyxl import load_workbook
from openpyxl import Workbook
import openpyxl
import datetime

def select(request):

    queryset = BusinessSupport.objects.all()
    queryset.delete() # 일괄 delete 요청    
    rawdata = Approval.objects.raw('select tmp4.*, deposit.transaction_content, deposit.deposit_number FROM ( select tmp3.*, settlement.billing_date, settlement.billing_amount FROM ( SELECT tmp2.*, delivery.in_date, delivery.in_amount, delivery.delivery_date FROM ( SELECT tmp1.*,order_data.order_num, order_data.order_date, order_data.order_quantity, order_data.assignment, order_data.scheduled_delivery_date FROM ( SELECT proposal.*, approval.approval_quantity, approval.quote_num, approval.approval_unit, approval.approval_price FROM proposal LEFT JOIN approval ON proposal.oppty_num=approval.oppty_num AND proposal.productno=approval.productno AND proposal.recipient=approval.recipient) tmp1 LEFT JOIN order_data ON tmp1.oppty_num=order_data.oppty_num AND tmp1.productno=order_data.productno AND tmp1.recipient=order_data.recipient AND tmp1.quote_num=order_data.quote_num ) tmp2 LEFT JOIN delivery ON delivery.order_num=tmp2.order_num AND delivery.company_registration_number=tmp2.company_registration_number) tmp3 LEFT JOIN settlement ON settlement.order_num=tmp3.order_num AND settlement.quote_num=tmp3.quote_num AND settlement.oppty_num=tmp3.oppty_num AND settlement.productno=tmp3.productno AND settlement.recipient=tmp3.recipient ) tmp4 LEFT JOIN deposit ON tmp4.company_registration_number = deposit.company_registration_number')
    
    for i in rawdata:
        data = BusinessSupport()
        data.team = i.team
        data.sales_manager = i.sales_manager
        data.payment_method = i.payment_method
        data.main_category = i.main_category
        data.buy_place = i.buy_place
        data.sales_price = i.sales_price
        data.delivery_date = i.delivery_date
        data.billing_date = i.billing_date
        data.billing_place = i.billing_place
        data.billing_amount = i.billing_amount
        data.in_amount = i.in_amount
        data.in_date = i.in_date
        data.transaction_content = i.transaction_content
        data.approval_price_net = (i.approval_price / 1.1)
        data.sales_price_net = (i.sales_price / 1.1)
        #주문액 순매입
        ##########################################################################

        data.first_margin = (i.sales_price / 1.1) 
        # 
        data.commission_income = 0
        # commission_income = 주문액순매입*(제품등록내 전문성수수료+잠재력수수료)
        ##########################################################################

        data.collaboration_income = (i.approval_price / 1.1) * 0
        # =승인액순매입*임직원등록내 수수료율
        ##########################################################################

        data.broker_income = i.broker_income
        data.net_sales_profit = i.net_sales_profit
        data.collaboration_cost = i.collaboration_cost
        data.inno_profit = i.inno_profit
        data.overload = i.overload
        data.credit_card_financial_cost = i.credit_card_financial_cost
        data.credit_cost = i.credit_cost
        data.credit_date = i.credit_date
        data.scheduled_delivery_month = i.scheduled_delivery_month
        data.delivery_month = i.delivery_month
        data.settlement_month = i.settlement_month
        data.order_num = i.order_num
        data.quote_num = i.quote_num
        data.oppty_num = i.oppty_num
        data.productno = i.productno
        data.recipient = i.recipient
        data.company_registration_number = i.company_registration_number
        data.deposit_number = i.deposit_number
        data.save()

    business_support_data = BusinessSupport.objects.all()
    
    return business_support_data

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
