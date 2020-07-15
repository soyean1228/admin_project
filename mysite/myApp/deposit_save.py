from .models import Deposit

def save(request):
    print("deposit_save")

    for i in range(0,5):

        customer_name = None;  deposit_amount = None; balance = None; 
        payment_method = None; deposit_date = None; order_num = None; scheduled_shipping_date = None; 

        customer_name = request.POST.get('customer_name' + str(i),'')
        deposit_amount = request.POST.get('deposit_amount' + str(i),0)
        if deposit_amount == '' : 
            deposit_amount = None
        balance = request.POST.get('balance' + str(i),0)
        if balance == '' : 
            balance = None
        payment_method = request.POST.get('payment_method' + str(i),'')
        if payment_method == '' : 
            payment_method = None
        deposit_date = request.POST.get('deposit_date' + str(i),0)
        if deposit_date == '' : 
            deposit_date = None
        order_num = request.POST.get('order_num' + str(i),0)
        if order_num == '' : 
            order_num = None
        scheduled_shipping_date = request.POST.get('scheduled_shipping_date' + str(i),0)
        if scheduled_shipping_date == '' : 
            scheduled_shipping_date = None

        if customer_name != '' :
            deposit_data = Deposit(customer_name, deposit_amount, balance, payment_method, deposit_date, order_num, scheduled_shipping_date) 
            deposit_data.save()

    print("완료")
    