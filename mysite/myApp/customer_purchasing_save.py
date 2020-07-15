from .models import CustomerPurchasing

def save(request):
    print("customer_purchasing_save")

    for i in range(0,5):
        customer_purchasing_manager = None; company_registration_number = None; 
        contact_number1 = None; contact_number2 = None; email = None; 

        customer_purchasing_manager = request.POST.get('customer_purchasing_manager' + str(i), None)
        company_registration_number = request.POST.get('company_registration_number' + str(i), None)
        if company_registration_number == '' : 
            company_registration_number = None
        contact_number1 = request.POST.get('contact_number1' + str(i), None)
        if contact_number1 == '' : 
            contact_number1 = None
        contact_number2 = request.POST.get('contact_number2' + str(i), None)
        if contact_number2 == '' : 
            contact_number2 = None
        email = request.POST.get('email' + str(i), None)
        if email == '' : 
            email = None

        # print(customer_purchasing_manager)

        if customer_purchasing_manager != '' :
            customer_purchasing_data = CustomerPurchasing (customer_purchasing_manager, company_registration_number, contact_number1, contact_number2, email) 
            customer_purchasing_data.save()

    print("완료")
