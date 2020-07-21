from .models import OrderData
from .models import Approval
from django.core.exceptions import ObjectDoesNotExist

def save(request):
    print("order_save")

    for i in range(0,5):

        order_num = None;  oppty_num = None; product_model_name = None; 
        order_quantity = None; order_date = None; quote_num = None; scheduled_delivery_date = None; 
        assignment = None;  recipient = None; recipient_phone = None; delivery_address = None; 
        balance = None;  order_close = None 

        order_num = request.POST.get('order_num' + str(i),0)
        oppty_num = request.POST.get('oppty_num' + str(i),0)
        if oppty_num == '' : 
            oppty_num = None
        product_model_name = request.POST.get('product_model_name' + str(i),0)
        if product_model_name == '' : 
            product_model_name = None
        order_quantity = request.POST.get('order_quantity' + str(i),0)
        if order_quantity == '' : 
            order_quantity = None
        order_date = request.POST.get('order_date' + str(i),0)
        if order_date == '' : 
            order_date = None
        quote_num = request.POST.get('quote_num' + str(i),0)
        if quote_num == '' : 
            quote_num = None
        scheduled_delivery_date = request.POST.get('scheduled_delivery_date' + str(i),0)
        if scheduled_delivery_date == '' : 
            scheduled_delivery_date = None
        assignment = request.POST.get('assignment' + str(i),0)
        if assignment == '' : 
            assignment = None
        recipient = request.POST.get('recipient' + str(i),0)
        if recipient == '' : 
            recipient = None
        recipient_phone = request.POST.get('recipient_phone' + str(i),0)
        if recipient_phone == '' : 
            recipient_phone = None
        delivery_address = request.POST.get('delivery_address' + str(i),0)
        if delivery_address == '' : 
            delivery_address = None
        balance = request.POST.get('balance' + str(i),0)
        order_close = request.POST.get('order_close' + str(i),0)
        if order_close == '' : 
            order_close = None

        if order_num != '' :
            if balance == '' : 
                # 입력이 안되었으면 자동으로 계산되도록 
                # 수량 = 승인수량 - 주문수량
                # balance = Approval.approval_quantity - order_quantity 
                try :
                    row = Approval.objects.get(quote_num =quote_num )
                    if order_quantity != None and row.approval_quantity != None:  
                        print(row.approval_quantity)
                        print(" - ")
                        print(order_quantity)
                        balance = row.approval_quantity - int(order_quantity)
                    elif row.approval_quantity != None and order_quantity == None:
                        balance = row.approval_quantity
                    else:
                        balance = None
                except ObjectDoesNotExist:
                    print("예외")
                    balance = None
            OrderData_data = OrderData(order_num, oppty_num, product_model_name, order_quantity, 
                            order_date, quote_num, scheduled_delivery_date,assignment, recipient, 
                            recipient_phone, delivery_address, balance, order_close) 
            OrderData_data.save()

    print("완료")
    