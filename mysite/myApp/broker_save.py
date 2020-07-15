from .models import Broker

def save(request):
    print("broker_save")

    for i in range(0,5):
        name = None; resident_registration_number = None; addresss = None; 
        contact_number = None; fee = None; 

        name = request.POST.get('name' + str(i), None)
        resident_registration_number = request.POST.get('resident_registration_number' + str(i), None)
        if resident_registration_number == '' : 
            resident_registration_number = None
        addresss = request.POST.get('addresss' + str(i), None)
        if addresss == '' : 
            addresss = None
        contact_number = request.POST.get('contact_number' + str(i), None)
        if contact_number == '' : 
            contact_number = None
        fee = request.POST.get('fee' + str(i), None)
        if fee == '' : 
            fee = None

        # print(name)

        if name != '' :
            broker_data = Broker (name, resident_registration_number, addresss, contact_number, fee) 
            broker_data.save()

    print("완료")
