from .models import Sales
from .models import SalesContent
from .models import Approval
from .models import OrderData
from .models import Deposit
from .models import Delivery
from .models import Scm

def select(request):
    samsung_code = request.POST.get('samsung_code',0)
    samsung_manager = request.POST.get('samsung_manager',0)
    sales_manager = request.POST.get('sales_manager',0)
    scm_manager = request.POST.get('scm_manager',0)
    customer_name = request.POST.get('customer_name',0)

    print(samsung_code)
    print(samsung_manager)
    print(sales_manager)
    print(scm_manager)
    print(customer_name)

    recipient = request.POST.get('recipient',0)
    delivery_address = request.POST.get('delivery_address',0)
    recipient_phone = request.POST.get('recipient_phone',0)
    product_model_name = request.POST.get('product_model_name',0)
    beginning_purchase = request.POST.get('beginning_purchase',0)
    
    print(recipient)
    print(delivery_address)
    print(recipient_phone)
    print(product_model_name)
    print(beginning_purchase)

    order_quantity = request.POST.get('order_quantity',0)
    approval_price = request.POST.get('approval_price',0)
    approval_total_price = request.POST.get('approval_total_price',0)
    sales_price = request.POST.get('sales_price',0)
    sales_total_price = request.POST.get('sales_total_price',0)
    
    print(order_quantity)
    print(approval_price)
    print(approval_total_price)
    print(sales_price)
    print(sales_total_price)

    oppty_num = request.POST.get('oppty_num',0)
    quote_num = request.POST.get('quote_num' ,0)
    order_date = request.POST.get('order_date' ,0)
    order_num = request.POST.get('order_num',0)
    delivery_request_date = request.POST.get('delivery_request_date',0)
    
    print(oppty_num)
    print(quote_num)
    print(order_date)
    print(order_num)
    print(delivery_request_date)

    scheduled_delivery_date = request.POST.get('scheduled_delivery_date',0)
    assignment = request.POST.get('assignment',0)
    deposit_date = request.POST.get('deposit_date',0)
    deposit_amount = request.POST.get('deposit_amount',0)
    billing_place =  request.POST.get('billing_place',0)


    print(scheduled_delivery_date)
    print(assignment)
    print(deposit_date)
    print(deposit_amount)
    print(billing_place)

    # data = Sales.objects.raw('select * from sales,sales_content,approval,order_data,deposit,delivery where sales_content.oppty_num = sales.oppty_num and sales.oppty_num = approval.oppty_num and order_data.order_num = deposit.order_num and order_data.order_num = delivery.order_num')
   
    # sales와 sales_content와 approval 까지의 join 
    # 계약은 전체가 보임 -> 계약 하나와 관련한 거래 내용 보이기 
    # 계약 하나에 승인 여러개 가능 
    # data = Sales.objects.raw('select * from sales left join sales_content on sales.oppty_num = sales_content.oppty_num left join approval on sales.oppty_num = approval.oppty_num ')
    
    Scm.objects.raw('DELETE FROM scm')
    Scm.objects.raw('INSERT INTO scm SELECT temp.oppty_num, temp.samsung_code, temp.samsung_manager, temp.sales_manager, temp.scm_manager, temp.customer_name, temp.recipient, temp.delivery_address, temp.recipient_phone, temp.product_model_name, temp.beginning_purchase, temp.order_quantity, temp.approval_price, temp.sales_price, temp.quote_num, temp.order_date, temp.order_num, temp.delivery_request_date, temp.scheduled_delivery_date, temp.assignment, temp.billing_place FROM ( select sales.oppty_num, sales.samsung_code, sales.samsung_manager, sales.sales_manager, sales.scm_manager, sales.customer_name, sales_content.recipient, sales_content.delivery_address, sales_content.recipient_phone, sales_content.product_model_name, sales_content.beginning_purchase, order_data.order_quantity, approval.approval_price, sales_content.sales_price, order_data.quote_num, order_data.order_date, order_data.order_num, sales_content.delivery_request_date, order_data.scheduled_delivery_date, order_data.assignment, sales.billing_place from sales left join sales_content on sales.oppty_num = sales_content.oppty_num left join approval on sales.oppty_num = approval.oppty_num left join order_data on sales.oppty_num = order_data.oppty_num ) temp LEFT JOIN delivery ON temp.order_num = delivery.order_num LEFT JOIN deposit ON temp.order_num = deposit.order_num')
    
    # query = 'select * from scm'

    # data = Scm.objects.raw(query)

    data = Scm.objects.all()
    
    query = ''
    if samsung_code != '' : 
        str = 'samsung_code=' + samsung_code
        query += str
        print(query)
    # elif samsung_manager != '' : 

    # elif sales_manager != '' : 

    # elif scm_manager != '' : 

    # elif customer_name != '' : 

    data = data.filter(query)

    return data