from .models import Deposit
from .models import CustomerDepositBalance

def save(request):
    print("deposit_save")

    isSuccess = "저장에 실패했습니다"   

    for i in range(0,1):

        company_registration_number = None;  order_num = None; 
        deposit_number = None; transaction_date = None 
        transaction_content = None; in_amount = None; 
        out_amount = None; deposit_balance = None; 
        
        company_registration_number = request.POST.get('select_company_registration_number',0)
        customer_name = request.POST.get('select_customer_name',0)
        order_num = request.POST.get('order_num' + str(i),'')
        if order_num == '' : 
            order_num = None
        # deposit_number = request.POST.get('deposit_number' + str(i),0)
        # if deposit_number == '' : 
        #     deposit_number = None
        
        #미구현
        deposit_number = 0
        
        transaction_date = request.POST.get('transaction_date' + str(i),0)
        if transaction_date == '' : 
            transaction_date = None
        transaction_content = request.POST.get('transaction_content' + str(i),'')
        if transaction_content == '' : 
            transaction_content = None
        in_amount = request.POST.get('in_amount' + str(i),0)
        if in_amount == '' : 
            in_amount = None
        
        # 잔액
        deposit_balance = in_amount

        if order_num != '' :
            deposit_data = Deposit(customer_name, company_registration_number, deposit_number, transaction_date, transaction_content, in_amount, out_amount, deposit_balance, order_num) 
            deposit_data.save()
            
            customer_deposit_data = CustomerDepositBalance ( company_registration_number, deposit_balance)
            customer_deposit_data.save()
        isSuccess = "저장되었습니다"  
    
    return isSuccess
    