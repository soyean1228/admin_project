from .models import Broker

def save(request):
    print("broker_save")

    for i in range(0,1):
        name = None; resident_registration_number = None; addresss = None; 
        contact_number = None; fee = None; team = None; manager = None

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
        team = request.POST.get('team' + str(i), None)
        if team == '' : 
            team = None
        manager = request.POST.get('manager' + str(i), None)
        if manager == '' : 
            manager = None

        if name != '':
            broker_data = Broker(name, resident_registration_number, addresss, contact_number, fee, team, manager)
            broker_data.save()

    print("완료")
