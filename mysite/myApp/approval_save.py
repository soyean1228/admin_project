from .models import Approval
from .models import Proposal
from .models import OrderData
# from .models import SalesContent
from django.core.exceptions import ObjectDoesNotExist

def save(request):
    print("approval_save")
    isSuccess = "저장에 실패했습니다"   

    oppty_num = request.POST.get('select_oppty_num',0)
    proposal_data_length = request.POST.get('proposal_data_length',0)
    # print(proposal_data_length)
    for i in range(0, int(proposal_data_length) + 1):
        # print(i)
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
            approval_balance = approval_quantity
            # 승인 잔량 = approval_quantity - - OrderData.order_quantity ( 그 견적번호의 주문수량의 합)
            # try :
            #     quote_num_order_data = OrderData.objects.filter(quote_num=quote_num)
            #     order_quantity_sum = 0
            #     for i in quote_num_order_data : 
            #         order_quantity_sum = order_quantity_sum + int(i.order_quantity)
            #     print(approval_quantity)
            #     print(order_quantity_sum)
            #     approval_balance = approval_quantity - order_quantity_sum
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

            approval_price = int(approval_quantity) * int(approval_unit)

            total_approval_balance = 0
            if Approval.objects.filter(quote_num=quote_num).count() == 0 :
                total_approval_balance = int(approval_price)
            else :
                approval = Approval.objects.filter(quote_num=quote_num)
                total_approval_balance = 0
                for i in approval : 
                    if i.approval_price != None :
                        if i.oppty_num != oppty_num or i.productno != productno or i.recipient != recipient :
                            total_approval_balance = total_approval_balance + int(i.approval_price)
                total_approval_balance = total_approval_balance + int(approval_price)

                # for i in Approval.objects.filter(quote_num=quote_num) : 
                #     print(i.total_approval_balance)
                #     i.total_approval_balance = total_approval_balance
                #     i.save
                
                Approval.objects.filter(quote_num=quote_num).update(total_approval_balance=total_approval_balance)

            data_count = Approval.objects.filter(quote_num=quote_num, productno=productno,recipient=recipient, oppty_num=oppty_num).count()
            if data_count != 0 :
                data = Approval.objects.get(quote_num=quote_num, productno=productno, recipient=recipient, oppty_num=oppty_num)
                data.delete()
            Approval.objects.create(quote_num=quote_num, oppty_num=oppty_num, productno=productno, recipient=recipient, approval_quantity=approval_quantity, approval_unit=approval_unit,
                                    approval_price=approval_price, approval_balance=approval_balance, total_approval_balance=total_approval_balance )
        
        isSuccess = "저장되었습니다"  
    
    return isSuccess