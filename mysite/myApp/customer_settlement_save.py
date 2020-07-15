from .models import CustomerSettlement

def save(request):
    print("customer_settlement_save")

    for i in range(0,5):
        customer_settlement_manager = None; company_registration_number = None; 
        contact_number = None; email = None; 

        customer_settlement_manager = request.POST.get('customer_settlement_manager' + str(i), None)
        company_registration_number = request.POST.get('company_registration_number' + str(i), None)
        if company_registration_number == '' : 
            company_registration_number = None
        contact_number = request.POST.get('contact_number' + str(i), None)
        if contact_number == '' : 
            contact_number = None
        email = request.POST.get('email' + str(i), None)
        if email == '' : 
            email = None

        # print(customer_settlement_manager)

        if customer_settlement_manager != '' :
            customer_settlement_data = CustomerSettlement (customer_settlement_manager, company_registration_number, contact_number, email) 
            customer_settlement_data.save()

    print("완료")
