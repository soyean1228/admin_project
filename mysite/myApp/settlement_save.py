from .models import Proposal
from .models import Settlement
from django.core.exceptions import ObjectDoesNotExist

def save(request):
    print("settlement_save")

    isSuccess = "저장에 실패했습니다"   
    select_delivery_date_start = request.POST.get('select_delivery_date_start',0)
    select_delivery_date_end = request.POST.get('select_delivery_date_end',0)
    select_customer_name = request.POST.get('select_customer_name',0)
    data_length = request.POST.get('data_length',0)
    print(data_length)
    for i in range(0, int(data_length) + 1):

        order_num = None; quote_num = None; oppty_num = None
        productno = None; recipient = None; billing_date = None
        billing_amount = None; settlement_month = None
        
        order_num = request.POST.get('order_num' + str(i),'')
        quote_num = request.POST.get('quote_num' + str(i),'')
        oppty_num = request.POST.get('oppty_num' + str(i),'')
        productno = request.POST.get('productno' + str(i),'')
        recipient = request.POST.get('recipient' + str(i),'')

        billing_place = request.POST.get('billing_place' + str(i),'')
        if billing_place == '' : 
            billing_place = None
        billing_date = request.POST.get('billing_date' + str(i),'')
        if billing_date == '' : 
            billing_date = None
        billing_amount = request.POST.get('sales_price' + str(i),0)
        if billing_amount == '' : 
            billing_amount = None
        settlement_month = request.POST.get('settlement_month' + str(i),0)
        if settlement_month == '' : 
            settlement_month = None

        if billing_date != '' :
            
            print(oppty_num)
            print(productno)
            print(recipient)
            proposal_data= Proposal.objects.filter(oppty_num=oppty_num,productno=productno,recipient=recipient)
            proposal_data.update(billing_place=billing_place)

            settlement_data = Settlement(order_num, quote_num , oppty_num, productno, recipient, billing_date, billing_amount, settlement_month) 
            settlement_data.save()
            isSuccess = "저장되었습니다"  
    
    return isSuccess
    