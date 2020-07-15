from .models import Delivery
from .models import OrderData
from django.core.exceptions import ObjectDoesNotExist

def save(request):
    print("delivery_save")

    for i in range(0,5):

        order_num = None;  quantity = None; delivery_date = None; 
        return_date = None; balance = None; 
        
        order_num = request.POST.get('order_num' + str(i),'')
        quantity = request.POST.get('quantity' + str(i),'')
        if quantity == '' : 
            quantity = None
        delivery_date = request.POST.get('delivery_date' + str(i),0)
        if delivery_date == '' : 
            delivery_date = None
        # print(delivery_date)
        return_date = request.POST.get('return_date' + str(i),0)
        if return_date == '' : 
            return_date = None

        balance = request.POST.get('balance' + str(i), None)

        if order_num != '' :
            if balance == '' : 
                # 입력이 안되었으면 자동으로 계산되도록 
                # balance = OrderData.order_quantity - quantity
                try :
                    row = OrderData.objects.get(order_num=order_num)
                    if quantity != None and row.order_quantity != None:  
                        balance = row.order_quantity - quantity
                    elif row.order_quantity != None and quantity == None:
                        balance = row.order_quantity
                    else:
                        balance = None
                except ObjectDoesNotExist:
                    print("예외")
                    balance = None
            delivery_data = Delivery(order_num, quantity, delivery_date, return_date, balance) 
            delivery_data.save()

    print("완료")
    