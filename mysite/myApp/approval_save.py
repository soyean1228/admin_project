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
        decision_quantity = request.POST.get('decision_quantity' + str(i),0)
        if int(approval_quantity) > int(decision_quantity) :
            print(approval_quantity)
            print(decision_quantity)
            return "승인수량은 품의수량보다 작아야 합니다"

        approval_unit = request.POST.get('approval_unit' + str(i),0)
        if approval_unit == '' : 
            approval_unit = 0

        if quote_num != '' and productno != '' and oppty_num != '' and recipient != '':
            approval_balance = approval_quantity
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
                
                Approval.objects.filter(quote_num=quote_num).update(total_approval_balance=total_approval_balance)

            data_count = Approval.objects.filter(quote_num=quote_num, productno=productno,recipient=recipient, oppty_num=oppty_num).count()
            if data_count != 0 :
                data = Approval.objects.get(quote_num=quote_num, productno=productno, recipient=recipient, oppty_num=oppty_num)
                data.delete()
            Approval.objects.create(quote_num=quote_num, oppty_num=oppty_num, productno=productno, recipient=recipient, approval_quantity=approval_quantity, approval_unit=approval_unit,
                                    approval_price=approval_price, approval_balance=approval_balance, total_approval_balance=total_approval_balance )
            # proposal의 proposal_balance 구현
            proposal_data = Proposal.objects.filter(oppty_num=oppty_num,productno=productno,recipient=recipient)
            proposal_balance = proposal_data.first().proposal_balance - int(approval_quantity)
            proposal_data.update(proposal_balance=proposal_balance)
        isSuccess = "저장되었습니다"  
    
    return isSuccess

def modify(request):
    print("modify_approval")
    modify_select_quote_num = request.POST.get('modify_select_quote_num','')
    modify_select_oppty_num = request.POST.get('modify_select_oppty_num','')
    modify_select_product_no = request.POST.get('modify_select_product_no','')
    modify_select_recipient = request.POST.get('modify_select_recipient','')
    approval_data = Approval.objects.raw('SELECT approval. *,  proposal.buy_place, proposal.decision_quantity,  proposal.delivery_request_date  FROM  approval INNER JOIN proposal ON approval.oppty_num = proposal.oppty_num AND approval.productno = proposal.productno AND approval.recipient = proposal.recipient ;')
    result_data = []
    for i in approval_data :
        isInsert = 0
        if modify_select_quote_num != '':
            if int(i.quote_num) == int(modify_select_quote_num):
                isInsert = 1
            else : 
                isInsert = 0 
                continue
        if modify_select_oppty_num != '':
            if i.oppty_num == modify_select_oppty_num:
                isInsert = 1
            else : 
                isInsert = 0 
                continue
        if modify_select_product_no != '':
            if i.productno == modify_select_product_no:
                isInsert = 1
            else : 
                isInsert = 0 
                continue
        if modify_select_recipient != '':
            if i.recipient == modify_select_recipient:
                isInsert = 1
            else : 
                isInsert = 0 
                continue
        if isInsert == 1:
            result_data.append(i)
    return result_data

def modify_save(request):
    print("modify_save")
    isSuccess = "수정에 실패했습니다"   

    modify_select_data_length = request.POST.get('modify_select_data_length','')
    for i in range(0, int(modify_select_data_length) + 1):
        productno = None; approval_quantity = None; 
        approval_price = None; quote_num = None; approval_balance = None; 
        decision_quantity = None; approval_unit = None; buy_place = None; 
        delivery_request_date = None; total_approval_balance = None
        recipient = None; oppty_num = None; quote_num = None; 

        quote_num = request.POST.get('modify_quote_num' + str(i),'')
        oppty_num = request.POST.get('modify_oppty_num' + str(i),'')
        productno = request.POST.get('modify_productno' + str(i),'')
        recipient = request.POST.get('modify_recipient' + str(i),'')

        approval_quantity = request.POST.get('modify_approval_quantity' + str(i),0)
        if approval_quantity == '' : 
            approval_quantity = 0
        decision_quantity = request.POST.get('modify_decision_quantity' + str(i),0)
        if int(approval_quantity) > int(decision_quantity) :
            return "승인수량은 품의수량보다 작아야 합니다"

        approval_unit = request.POST.get('modify_approval_unit' + str(i),0)
        if approval_unit == '' : 
            approval_unit = 0

        approval_price = int(approval_quantity) * int(approval_unit)

        approval_balance = request.POST.get('modify_approval_balance' + str(i),0)
        if approval_balance == '' : 
            approval_balance = 0

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
            
            Approval.objects.filter(quote_num=quote_num).update(total_approval_balance=total_approval_balance)

        if quote_num != '' and productno != '' and oppty_num != '' and recipient != '':
            data_count = Approval.objects.filter(quote_num=quote_num, oppty_num=oppty_num, recipient=recipient, productno=productno).count()
            if data_count != 0 :
                data = Approval.objects.get(quote_num=quote_num, oppty_num=oppty_num, recipient=recipient, productno=productno)
                data.delete()
            Approval.objects.create(quote_num=quote_num, oppty_num=oppty_num, productno=productno, recipient=recipient, approval_quantity=approval_quantity, approval_unit=approval_unit,
                                    approval_price=approval_price, approval_balance=approval_balance, total_approval_balance=total_approval_balance )
            # proposal의 proposal_balance 구현
            proposal_data = Proposal.objects.filter(oppty_num=oppty_num,productno=productno,recipient=recipient)
            proposal_balance = proposal_data.first().proposal_balance - int(approval_quantity)
            proposal_data.update(proposal_balance=proposal_balance)
            isSuccess = "수정되었습니다"  
        else :
            isSuccess = "수정에 실패했습니다"

    return isSuccess