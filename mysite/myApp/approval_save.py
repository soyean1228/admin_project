from .models import Approval
from .models import Proposal
# from .models import SalesContent
from django.core.exceptions import ObjectDoesNotExist

def save(request):
    print("approval_save")
    isSuccess = "저장에 실패했습니다"   

    oppty_num = request.POST.get('select_oppty_num',0)
    proposal_data_length = request.POST.get('proposal_data_length',0)
    print(proposal_data_length)
    for i in range(0, int(proposal_data_length) + 1):
        print(i)
        productno = None; approval_quantity = None; 
        approval_price = None; quote_num = None; approval_balance = None; 
        decision_quantity = None; approval_unit = None; buy_place = None; 
        delivery_request_date = None; total_approval_balance = None
        recipient = None

        quote_num = request.POST.get('quote_num' + str(i),0)
        productno = request.POST.get('productno' + str(i),'')
        recipient = request.POST.get('recipient' + str(i),'')

        approval_quantity = request.POST.get('approval_quantity' + str(i),0)
        if approval_quantity == '' : 
            approval_quantity = 0
        approval_unit = request.POST.get('approval_unit' + str(i),0)
        if approval_unit == '' : 
            approval_unit = 0

        print(quote_num)
        print(productno)
        if quote_num != '' and productno != '' and oppty_num != '' and recipient != '':
            # if balance == '' : 
                # 입력이 안되었으면 자동으로 계산되도록 
                # 수량 = 거래수량 - 승인수량
                # balance = SalesContent.decision_quantity - approval_quantity 
                # try :
                #     row = SalesContent.objects.get(oppty_num=oppty_num)
                #     if approval_quantity != None and row.decision_quantity != None:  
                #         print(row.decision_quantity)
                #         print("-")
                #         print(approval_quantity)
                #         balance = row.decision_quantity - int(approval_quantity)
                #     elif row.decision_quantity != None and approval_quantity == None:
                #         balance = row.decision_quantity
                #     else:
                #         balance = None
                # except ObjectDoesNotExist:
                #     print("예외")
                #     balance = None
            # 미구현
            approval_balance = 0
            # approval_balance = approval_quantity - OrderData.approval_quantity 
            # try :
            #     row = SalesContent.objects.get(oppty_num=oppty_num)
            #     if approval_quantity != None and row.decision_quantity != None:  
            #         print(row.decision_quantity)
            #         print("-")
            #         print(approval_quantity)
            #         balance = row.decision_quantity - int(approval_quantity)
            #     elif row.decision_quantity != None and approval_quantity == None:
            #         balance = row.decision_quantity
            #     else:
            #         balance = None
            # except ObjectDoesNotExist:
            #     print("예외")
            #     balance = None
            total_approval_balance = 0


            approval_price = int(approval_quantity) * int(approval_unit)
            print(approval_price)

            data_count = Approval.objects.filter(quote_num=quote_num, productno=productno,recipient=recipient, oppty_num=oppty_num).count()
            print("data_count")
            print(data_count)
            if data_count != 0 :
                data = Approval.objects.get(quote_num=quote_num, productno=productno, recipient=recipient, oppty_num=oppty_num)
                data.delete()
            Approval.objects.create(quote_num=quote_num, oppty_num=oppty_num, productno=productno, recipient=recipient, approval_quantity=approval_quantity, approval_unit=approval_unit,
                                    approval_price=approval_price, approval_balance=approval_balance, total_approval_balance=total_approval_balance )
        
        isSuccess = "저장되었습니다"  
    
    return isSuccess