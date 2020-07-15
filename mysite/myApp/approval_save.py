from .models import Approval
from .models import SalesContent
from django.core.exceptions import ObjectDoesNotExist

def save(request):
    print("approval_save")

    for i in range(0,5):

        sales_num = None;  product_model_name = None; approval_quantity = None; 
        approval_price = None; quote_num = None; balance = None; 
        
        sales_num = request.POST.get('sales_num' + str(i),0)
        product_model_name = request.POST.get('product_model_name' + str(i),'')
        if product_model_name == '' : 
            product_model_name = None
        approval_quantity = request.POST.get('approval_quantity' + str(i),0)
        if approval_quantity == '' : 
            approval_quantity = None
        approval_price = request.POST.get('approval_price' + str(i),0)
        if approval_price == '' : 
            approval_price = None
        quote_num = request.POST.get('quote_num' + str(i),0)
        if quote_num == '' : 
            quote_num = None
        balance = request.POST.get('balance' + str(i),0)

        if sales_num != '' :
            if balance == '' : 
                # 입력이 안되었으면 자동으로 계산되도록 
                # 수량 = 거래수량 - 승인수량
                # balance = SalesContent.decision_quantity - order_quantity 
                try :
                    row = SalesContent.objects.get(sales_num=sales_num)
                    if order_quantity != None and row.decision_quantity != None:  
                        balance = row.decision_quantity - order_quantity
                    elif row.decision_quantity != None and order_quantity == None:
                        balance = row.decision_quantity
                    else:
                        balance = None
                except ObjectDoesNotExist:
                    print("예외")
                    balance = None
            approval_data = Approval(sales_num, product_model_name, approval_quantity, approval_price, quote_num, balance) 
            approval_data.save()

    print("완료")
    