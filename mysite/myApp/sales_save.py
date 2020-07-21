from .models import Sales

def save(request):
    print("sales_save")

    for i in range(0,5):
        samsung_code =''; samsung_manager = ''; point = ''; 
        sales_manager = ''; broker_name =''; scm_manager = ''; 
        customer_name = ''; payment_method =''; sales_type = ''; 
        demand = ''; billing_place =''; oppty_num = ''; 

        oppty_num = request.POST.get('oppty_num' + str(i), None)
        samsung_code = request.POST.get('samsung_code' + str(i), None)
        if samsung_code == '' : 
            samsung_code = None
        samsung_manager = request.POST.get('samsung_manager' + str(i), None)
        if samsung_manager == '' : 
            samsung_manager = None
        point = request.POST.get('point' + str(i), None)
        if point == '' : 
            point = None
        sales_manager = request.POST.get('sales_manager' + str(i), None)
        if sales_manager == '' : 
            sales_manager = None
        broker_name = request.POST.get('broker_name' + str(i), None)
        if broker_name == '' : 
            broker_name = None
        scm_manager = request.POST.get('scm_manager' + str(i), None)
        if scm_manager == '' : 
            scm_manager = None
        customer_name = request.POST.get('customer_name' + str(i), None)
        if customer_name == '' : 
            customer_name = None
        payment_method = request.POST.get('payment_method' + str(i), None)
        if payment_method == '' : 
            payment_method = None
        sales_type = request.POST.get('sales_type' + str(i), None)
        if sales_type == '' : 
            sales_type = None
        demand = request.POST.get('demand' + str(i), None)
        if demand == '' : 
            demand = None
        billing_place = request.POST.get('billing_place' + str(i), None)
        if billing_place == '' : 
            billing_place = None

        if oppty_num != '' :
            print(oppty_num)
            sales_data = Sales(samsung_code, samsung_manager, point, 
                            sales_manager, broker_name, scm_manager, 
                            customer_name, payment_method, sales_type, 
                            demand, billing_place, oppty_num ) 
            sales_data.save()

    print("완료")
    