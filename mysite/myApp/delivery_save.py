from .models import Delivery
from .models import Deposit
from .models import OrderData
from django.core.exceptions import ObjectDoesNotExist

def save(request):
    print("delivery_save")

    isSuccess = "저장에 실패했습니다"   

    data_length = request.POST.get('data_length',0)
    print(data_length)
    for i in range(0, int(data_length) + 1):

        order_num = None; in_date = None; in_amount = None; customer_name = None
        etc = None; delivery_date = None; company_registration_number = None
        
        order_num = request.POST.get('order_num' + str(i),'')
        in_date = request.POST.get('in_date' + str(i),'')
        if in_date == '' : 
            in_date = None
        in_amount = request.POST.get('in_amount' + str(i),0)
        if in_amount == '' : 
            in_amount = None
        etc = request.POST.get('etc' + str(i),0)
        if etc == '' : 
            etc = None
        delivery_date = request.POST.get('delivery_date' + str(i),0)
        if delivery_date == '' : 
            delivery_date = None
        company_registration_number = request.POST.get('company_registration_number' + str(i),0)
        print("company_registration_number")
        print(company_registration_number)
        if company_registration_number == '' : 
            company_registration_number = None
        customer_name = request.POST.get('customer_name' + str(i),0)
        if customer_name == '' : 
            customer_name = None

        if order_num != '' :
            delivery_data = Delivery(order_num, in_date, in_amount, etc, delivery_date) 
            delivery_data.save()

            # 돈이 들어오면, 
            deposit_data= Deposit.objects.filter(company_registration_number=company_registration_number)
            max_deposit_number = 0
            for i in deposit_data:
                if i.deposit_number >= max_deposit_number:
                    max_deposit_number = i.deposit_number
            max_deposit_number = max_deposit_number + 1
            print(max_deposit_number) 
            try : 
                if Deposit.objects.filter(company_registration_number=company_registration_number).count() == 1 :
                    # 아직 내역이 없으면
                    data = Deposit.objects.get(company_registration_number=company_registration_number,deposit_number=0)
                    transaction_date = data.transaction_date
                    transaction_content = data.transaction_content
                    deposit_balance = int(data.in_amount) - int(in_amount)  
                    deposit_data = Deposit.objects.create(customer_name=customer_name, company_registration_number=company_registration_number, deposit_number=max_deposit_number, transaction_date=transaction_date, transaction_content=transaction_content, in_amount=None, out_amount=in_amount, deposit_balance=deposit_balance, order_num=order_num) 
                else :
                    # 내역이 있으면 
                    data = Deposit.objects.get(company_registration_number=company_registration_number,deposit_number=0)
                    transaction_date = data.transaction_date
                    transaction_content = data.transaction_content
                    deposit_balance = int(data.deposit_balance) - int(in_amount)
                    deposit_data = Deposit.objects.create(customer_name=customer_name, company_registration_number=company_registration_number, deposit_number=max_deposit_number, transaction_date=transaction_date, transaction_content=transaction_content, in_amount=None, out_amount=in_amount, deposit_balance=deposit_balance, order_num=order_num) 
            except :
                return "저장된 입출금 정보가 없습니다."

        isSuccess = "저장되었습니다"  
    
    return isSuccess
    