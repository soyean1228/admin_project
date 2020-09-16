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

    #validation 체크
    for i in range(0, int(proposal_data_length) + 1):
        productno = None; approval_quantity = None; 
        approval_price = None; quote_num = None; approval_balance = None; 
        decision_quantity = None; approval_unit = None; buy_place = None; 
        delivery_request_date = None; total_approval_balance = None
        recipient = None; decision_price = None; proposal_balance=None; 

        quote_num = request.POST.get('quote_num' + str(i),0)
        productno = request.POST.get('productno' + str(i),'')
        recipient = request.POST.get('recipient' + str(i),'')

        approval_quantity = request.POST.get('approval_quantity' + str(i),0)
        if approval_quantity == '' : 
            approval_quantity = 0
        approval_unit = request.POST.get('approval_unit' + str(i),0)
        if approval_unit == '' : 
            approval_unit = 0
        decision_price = request.POST.get('decision_price' + str(i),0)
        if decision_price == '' : 
            decision_price = 0

        if quote_num != '' and productno != '' and oppty_num != '' and recipient != '':
            # 승인액 확인
            approval_data = Approval.objects.filter(oppty_num=oppty_num, productno=productno, recipient=recipient)
            if approval_data != None:
                approval_price_sum = 0    
                for a in approval_data:
                    approval_price_sum = approval_price_sum + a.approval_price
                approval_price = int(approval_quantity) * int(approval_unit)
                approval_price_sum = approval_price_sum + approval_price
                print(approval_price_sum)
                print(decision_price)
                if int(approval_price_sum) > int(decision_price) :
                    return "승인액은 품의액보다 작아야 합니다"
            else:
                approval_price = int(approval_quantity) * int(approval_unit)
                print(approval_price)
                print(decision_price)
                if int(approval_price) > int(decision_price) :
                    return "승인액은 품의액보다 작아야 합니다"
                
            # 승인수량 확인
            # proposal의 proposal_balance 구현
            proposal_data = Proposal.objects.filter(oppty_num=oppty_num,productno=productno,recipient=recipient)
            proposal_balance_result = proposal_data.first().proposal_balance - int(approval_quantity)
            print(proposal_balance_result)
            if int(proposal_balance_result) < 0 :
                return "승인수량은 품의수량보다 작아야 합니다"

    # print(proposal_data_length)
    for i in range(0, int(proposal_data_length) + 1):
        productno = None; approval_quantity = None; 
        approval_price = None; quote_num = None; approval_balance = None; 
        decision_quantity = None; approval_unit = None; buy_place = None; 
        delivery_request_date = None; total_approval_balance = None
        recipient = None; decision_price = None; proposal_balance=None; 

        quote_num = request.POST.get('quote_num' + str(i),0)
        productno = request.POST.get('productno' + str(i),'')
        recipient = request.POST.get('recipient' + str(i),'')

        approval_unit = request.POST.get('approval_unit' + str(i),0)
        if approval_unit == '' : 
            approval_unit = 0

        decision_price = request.POST.get('decision_price' + str(i),0)
        if decision_price == '' : 
            decision_price = 0

        if quote_num != '' and productno != '' and oppty_num != '' and recipient != '':
            data_count = Approval.objects.filter(quote_num=quote_num, productno=productno, recipient=recipient, oppty_num=oppty_num).count()
            approval_quantity = request.POST.get('approval_quantity' + str(i),0)
            if approval_quantity == '' : 
                approval_quantity = 0
            approval_balance = approval_quantity
            proposal_balance = request.POST.get('proposal_balance' + str(i),0)
            approval_price = int(approval_quantity) * int(approval_unit)

            print("data_count = ")
            print(data_count)
            if data_count != 0 :
                print("있음")
                data = Approval.objects.filter(quote_num=quote_num, productno=productno, recipient=recipient, oppty_num=oppty_num)
                proposal_data = Proposal.objects.filter(oppty_num=oppty_num,productno=productno,recipient=recipient)
                proposal_balance_result = proposal_data.first().proposal_balance + int(data.first().approval_quantity)
                proposal_data.update(proposal_balance=proposal_balance_result)
                data.delete()
                
            # proposal의 proposal_balance 구현
            proposal_data = Proposal.objects.filter(oppty_num=oppty_num,productno=productno,recipient=recipient)
            proposal_balance_result = proposal_data.first().proposal_balance - int(approval_quantity)
            proposal_data.update(proposal_balance=proposal_balance_result)

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
            
            Approval.objects.create(quote_num=quote_num, oppty_num=oppty_num, productno=productno, recipient=recipient, approval_quantity=approval_quantity, approval_unit=approval_unit,
                                    approval_price=approval_price, approval_balance=approval_balance, total_approval_balance=total_approval_balance )
        
        isSuccess = "저장되었습니다"  
    
    return isSuccess

def modify(request):
    print("modify_approval")
    modify_select_quote_num = request.POST.get('modify_select_quote_num','')
    modify_select_oppty_num = request.POST.get('modify_select_oppty_num','')
    modify_select_product_no = request.POST.get('modify_select_product_no','')
    modify_select_recipient = request.POST.get('modify_select_recipient','')
    approval_data = Approval.objects.raw('SELECT approval. *,  proposal.buy_place, proposal.proposal_balance, proposal.decision_quantity,  proposal.delivery_request_date, proposal.decision_price  FROM  approval INNER JOIN proposal ON approval.oppty_num = proposal.oppty_num AND approval.productno = proposal.productno AND approval.recipient = proposal.recipient ;')
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

    # 수정 작업 전 데이터
    previous_data_origin = Approval.objects.all()
    previous_data = []
    for i in previous_data_origin :
        previous_data.append(i)

    # 수정 전 해당 데이터 모두 삭제
    deleted_data = modify(request)
    approval_data = Approval.objects.raw('SELECT approval. *, proposal.proposal_balance, proposal.buy_place, proposal.decision_quantity,  proposal.delivery_request_date  FROM  approval INNER JOIN proposal ON approval.oppty_num = proposal.oppty_num AND approval.productno = proposal.productno AND approval.recipient = proposal.recipient ;')        
    for i in approval_data:
        for j in deleted_data:
            if i == j : 
                # proposal의 proposal_balance 구현
                proposal_data = Proposal.objects.filter(oppty_num=i.oppty_num,productno=i.productno,recipient=i.recipient)
                proposal_balance_result = proposal_data.first().proposal_balance + int(i.approval_quantity)
                proposal_data.update(proposal_balance=proposal_balance_result)
                i.delete()
                
    isSuccess = "수정에 실패했습니다"   
    
    # 수정
    modify_select_data_length = request.POST.get('modify_select_data_length','')
    for i in range(0, int(modify_select_data_length) + 1):
        productno = None; approval_quantity = None; 
        approval_price = None; quote_num = None; approval_balance = None; 
        decision_quantity = None; approval_unit = None; buy_place = None; 
        delivery_request_date = None; total_approval_balance = None
        recipient = None; oppty_num = None; quote_num = None; 
        decision_price = None; proposal_balance=None; 

        quote_num = request.POST.get('modify_quote_num' + str(i),'')
        oppty_num = request.POST.get('modify_oppty_num' + str(i),'')
        productno = request.POST.get('modify_productno' + str(i),'')
        recipient = request.POST.get('modify_recipient' + str(i),'')

        approval_unit = request.POST.get('modify_approval_unit' + str(i),0)
        if approval_unit == '' : 
            approval_unit = 0

        decision_price = request.POST.get('modify_decision_price' + str(i),0)
        if decision_price == '' : 
            decision_price = 0

        # approval_balance = request.POST.get('modify_approval_balance' + str(i),0)
        # if approval_balance == '' : 
        #     approval_balance = 0

        if quote_num != '' and productno != '' and oppty_num != '' and recipient != '':
            data_count = Approval.objects.filter(quote_num=quote_num, productno=productno,recipient=recipient, oppty_num=oppty_num).count()
            approval_quantity = request.POST.get('modify_approval_quantity' + str(i),0)
            if approval_quantity == '' : 
                approval_quantity = 0
            approval_balance = approval_quantity
            proposal_balance = request.POST.get('modify_proposal_balance' + str(i),0)
            approval_price = int(approval_quantity) * int(approval_unit)

            if data_count != 0 :
                print("있음")
                data = Approval.objects.filter(quote_num=quote_num, productno=productno, recipient=recipient, oppty_num=oppty_num)
                proposal_data = Proposal.objects.filter(oppty_num=oppty_num,productno=productno,recipient=recipient)
                proposal_balance_result = proposal_data.first().proposal_balance + int(data.first().approval_quantity)
                proposal_data.update(proposal_balance=proposal_balance_result)
                data.delete()
                
            # proposal의 proposal_balance 구현
            proposal_data = Proposal.objects.filter(oppty_num=oppty_num,productno=productno,recipient=recipient)
            proposal_balance_result = proposal_data.first().proposal_balance - int(approval_quantity)
            print(proposal_balance_result)
            
            approval_price = int(approval_quantity) * int(approval_unit)
            
            proposal_data.update(proposal_balance=proposal_balance_result)

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
            
            Approval.objects.create(quote_num=quote_num, oppty_num=oppty_num, productno=productno, recipient=recipient, approval_quantity=approval_quantity, approval_unit=approval_unit,
                                    approval_price=approval_price, approval_balance=approval_balance, total_approval_balance=total_approval_balance )
        
            isSuccess = "수정되었습니다"  

    # 수정 후 validation 체크 
    ## proposal 데이터에서 -1이 있으면 fail ( 승인 수량 조건 만족 validation )
    isFail = False 
    proposal_data = Proposal.objects.all()
    for i in proposal_data :
        if int(i.proposal_balance) < 0 :
            isSuccess = "승인수량은 품의수량보다 작아야 합니다"
            isFail = True
            break
        approval_data = Approval.objects.filter(oppty_num=i.oppty_num, productno=i.productno, recipient=i.recipient)
        if approval_data != None:
            approval_price_sum = 0    
            for a in approval_data:
                approval_price_sum = approval_price_sum + a.approval_price
            if int(approval_price_sum) > int(i.decision_price) :
                isSuccess = "승인액은 품의액보다 작아야 합니다"
                isFail = True
                break
    
    #수정 실패하면 previous_data 복원
    if isFail == True :
        queryset = Approval.objects.all()
        queryset.delete() # 일괄 delete 요청 
        print("복원")
        print(previous_data)
        for i in previous_data:
            Approval.objects.create(quote_num=i.quote_num, oppty_num=i.oppty_num, productno=i.productno, recipient=i.recipient, approval_quantity=i.approval_quantity, approval_unit=i.approval_unit,
                                    approval_price=i.approval_price, approval_balance=i.approval_balance, total_approval_balance=i.total_approval_balance )
        # proposal의 proposal_balance 다시 계산
        proposal_data = Proposal.objects.all()
        for i in proposal_data :
            approval_data = Approval.objects.filter(oppty_num=i.oppty_num, productno=i.productno, recipient=i.recipient)
            if approval_data != None:
                approval_quantity_sum = 0
                for j in approval_data:
                    approval_quantity_sum = approval_quantity_sum + j.approval_quantity
                update_data = Proposal.objects.filter(oppty_num=i.oppty_num, productno=i.productno, recipient=i.recipient)
                proposal_balance = update_data.first().decision_quantity - approval_quantity_sum
                update_data.update(proposal_balance=proposal_balance)


    # isFail = False
    # for i in range(0, int(modify_select_data_length) + 1):
    #     productno = None; approval_quantity = None; 
    #     approval_price = None; quote_num = None; approval_balance = None; 
    #     decision_quantity = None; approval_unit = None; buy_place = None; 
    #     delivery_request_date = None; total_approval_balance = None
    #     recipient = None; oppty_num = None; quote_num = None; 
    #     decision_price = None; proposal_balance=None; 

    #     quote_num = request.POST.get('modify_quote_num' + str(i),'')
    #     oppty_num = request.POST.get('modify_oppty_num' + str(i),'')
    #     productno = request.POST.get('modify_productno' + str(i),'')
    #     recipient = request.POST.get('modify_recipient' + str(i),'')

    #     approval_unit = request.POST.get('modify_approval_unit' + str(i),0)
    #     if approval_unit == '' : 
    #         approval_unit = 0

    #     decision_price = request.POST.get('modify_decision_price' + str(i),0)
    #     if decision_price == '' : 
    #         decision_price = 0

    #     if quote_num != '' and productno != '' and oppty_num != '' and recipient != '':
    #         data_count = Approval.objects.filter(quote_num=quote_num, productno=productno,recipient=recipient, oppty_num=oppty_num).count()
    #         approval_quantity = request.POST.get('modify_approval_quantity' + str(i),0)
    #         if approval_quantity == '' : 
    #             approval_quantity = 0
    #         approval_balance = approval_quantity
    #         proposal_balance = request.POST.get('modify_proposal_balance' + str(i),0)
    #         approval_price = int(approval_quantity) * int(approval_unit)

    #         # proposal의 proposal_balance > validation 체크
    #         proposal_data = Proposal.objects.filter(oppty_num=oppty_num,productno=productno,recipient=recipient)
    #         proposal_balance_result = proposal_data.first().proposal_balance - int(approval_quantity)
    #         print(proposal_balance_result)
    #         if int(proposal_balance_result) < 0 :
    #             isSuccess = "승인수량은 품의수량보다 작아야 합니다"
    #             isFail = True

    #         approval_data = Approval.objects.filter(oppty_num=oppty_num, productno=productno, recipient=recipient)
    #         if approval_data != None:
    #             approval_price_sum = 0    
    #             for a in approval_data:
    #                 approval_price_sum = approval_price_sum + a.approval_price
    #             approval_price = int(approval_quantity) * int(approval_unit)
    #             approval_price_sum = approval_price_sum + approval_price
    #             print(approval_price_sum)
    #             print(decision_price)
    #             if int(approval_price_sum) > int(decision_price) :
    #                 isSuccess = "승인액은 품의액보다 작아야 합니다"
    #                 isFail = True
    #         else:
    #             approval_price = int(approval_quantity) * int(approval_unit)
    #             print(approval_price)
    #             print(decision_price)
    #             if int(approval_price) > int(decision_price) :
    #                 isSuccess = "승인액은 품의액보다 작아야 합니다"
    #                 isFail = True
    
    # if isFail == True :
    #     #previous_data 복원
    #     for i in previous_data:
    #         Approval.objects.create(quote_num=i.quote_num, oppty_num=i.oppty_num, productno=i.productno, recipient=i.recipient, approval_quantity=i.approval_quantity, approval_unit=i.approval_unit,
    #                                 approval_price=i.approval_price, approval_balance=i.approval_balance, total_approval_balance=i.total_approval_balance )
    #         # proposal의 proposal_balance 구현
    #         proposal_data = Proposal.objects.filter(oppty_num=i.oppty_num,productno=i.productno,recipient=i.recipient)
    #         proposal_balance_result = proposal_data.first().proposal_balance - int(i.approval_quantity)
    #         proposal_data.update(proposal_balance=proposal_balance_result)
    #     return isSuccess

    

    return isSuccess