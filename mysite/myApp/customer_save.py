from .models import Customer

def save(request):
    print("customer_save")

    for i in range(0,5):
        customer_name = None; company_registration_number = None; representative = None; 
        address = None;  opening_date = None;  field1 = None; 
        field2 = None;  field3 = None;  sales_manager = None; 
        scm_manager = None;  rate = None;  

        customer_name = request.POST.get('customer_name' + str(i),'')
        company_registration_number = request.POST.get('company_registration_number' + str(i),'')
        if company_registration_number == '' : 
            company_registration_number = None
        representative = request.POST.get('representative' + str(i), None)
        if representative == '' : 
            representative = None
        address = request.POST.get('address' + str(i), None)
        if address == '' : 
            address = None
        opening_date = request.POST.get('opening_date' + str(i), None)
        if opening_date == '' : 
            opening_date = None
        field1 = request.POST.get('field1' + str(i), None)
        if field1 == '' : 
            field1 = None
        field2 = request.POST.get('field2' + str(i), None)
        if field2 == '' : 
            field2 = None
        field3 = request.POST.get('field3' + str(i), None)
        if field3 == '' : 
            field3 = None
        sales_manager = request.POST.get('sales_manager' + str(i), None)
        if sales_manager == '' : 
            sales_manager = None
        scm_manager = request.POST.get('scm_manager' + str(i), None)
        if scm_manager == '' : 
            scm_manager = None
        rate = request.POST.get('rate' + str(i), None)
        if rate == '' : 
            rate = None

        if customer_name != '' :
            customer_data = Customer(customer_name, company_registration_number, representative, address, opening_date,
            field1, field2, field3, sales_manager,  scm_manager, rate) 
            customer_data.save()

    print("완료")