from .models import Approval
from .models import OrderData
from .models import Deposit
from .models import Delivery
from .models import Scm

def select(request):
    samsung_code = request.POST.get('samsung_code',0)
    samsung_sales_manager = request.POST.get('samsung_sales_manager',0)
    sales_manager = request.POST.get('sales_manager',0)
    scm_manager = request.POST.get('scm_manager',0)

    oppty_num = request.POST.get('oppty_num',0)
    quote_num = request.POST.get('quote_num',0)
    order_num = request.POST.get('order_num',0)

    customer_name = request.POST.get('customer_name',0)
    billing_place = request.POST.get('billing_place',0)
    recipient = request.POST.get('recipient',0)
    delivery_address = request.POST.get('delivery_address',0)
    recipient_phone1 = request.POST.get('recipient_phone1',0)

    order_date_start = request.POST.get('order_date_start',0)
    order_date_end = request.POST.get('order_date_end',0)

    delivery_request_date_start = request.POST.get('delivery_request_date_start',0)
    delivery_request_date_end = request.POST.get('delivery_request_date_end',0)

    scheduled_delivery_date_start = request.POST.get('scheduled_delivery_date_start' ,0)
    scheduled_delivery_date_end = request.POST.get('scheduled_delivery_date_end' ,0)

    delivery_date_start = request.POST.get('delivery_date_start',0)
    delivery_date_end = request.POST.get('delivery_date_end',0)
  
    Scm.objects.raw('DELETE FROM scm')
    Scm.objects.raw('INSERT INTO scm SELECT tmp3.*, settlement.billing_date, settlement.billing_amount FROM ( SELECT tmp2.*, delivery.in_date, delivery.in_amount, delivery.delivery_date FROM ( SELECT tmp1.*,order_data.order_num, order_data.order_date, order_data.order_quantity, order_data.assignment, order_data.scheduled_delivery_date FROM ( SELECT proposal.*, approval.approval_quantity, approval.quote_num, approval.approval_unit, approval.approval_price FROM proposal LEFT JOIN approval ON proposal.oppty_num=approval.oppty_num AND proposal.productno=approval.productno AND proposal.recipient=approval.recipient) tmp1 LEFT JOIN order_data ON tmp1.oppty_num=order_data.oppty_num AND tmp1.productno=order_data.productno AND tmp1.recipient=order_data.recipient AND tmp1.quote_num=order_data.quote_num ) tmp2 LEFT JOIN delivery ON delivery.order_num=tmp2.order_num AND delivery.company_registration_number=tmp2.company_registration_number) tmp3 LEFT JOIN settlement ON settlement.order_num=tmp3.order_num AND settlement.quote_num=tmp3.quote_num AND settlement.oppty_num=tmp3.oppty_num AND settlement.productno=tmp3.productno AND settlement.recipient=tmp3.recipient;')

    data = Scm.objects.all()
    for i in data:
        print("i")
        print(i.order_num)
        print(i.quote_num)
        print(i.order_quantity)
        print(i.approval_quantity)
        print(i.decision_quantity)
        if i.order_num:
            i.amount = i.order_quantity
        elif i.quote_num:
            i.amount = i.approval_quantity
        else:
            i.amount = i.decision_quantity
        print(i.amount)
        i.save()
    
    return data