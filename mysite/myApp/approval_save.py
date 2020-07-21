from .models import Approval
from .models import SalesContent
from django.core.exceptions import ObjectDoesNotExist

def save(request):
    print("approval_save")

    for i in range(0,5):

        oppty_num = None;  product_model_name = None; approval_quantity = None; 
        approval_price = None; quote_num = None; balance = None; 
        
        oppty_num = request.POST.get('oppty_num' + str(i),0)
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

        if oppty_num != '' :
            if balance == '' : 
                # 입력이 안되었으면 자동으로 계산되도록 
                # 수량 = 거래수량 - 승인수량
                # balance = SalesContent.decision_quantity - approval_quantity 
                try :
                    row = SalesContent.objects.get(oppty_num=oppty_num)
                    if approval_quantity != None and row.decision_quantity != None:  
                        print(row.decision_quantity)
                        print("-")
                        print(approval_quantity)
                        balance = row.decision_quantity - int(approval_quantity)
                    elif row.decision_quantity != None and approval_quantity == None:
                        balance = row.decision_quantity
                    else:
                        balance = None
                except ObjectDoesNotExist:
                    print("예외")
                    balance = None
            approval_data = Approval(quote_num,oppty_num, product_model_name, approval_quantity, approval_price, balance) 
            approval_data.save()

    print("완료")
    