from .models import Employee

def save(request):

    print("employee_save")

    for i in range(0,5):

        name = None; position = None; department = None;  phone_num = None;  office_num = None;  address = None; 
        name = request.POST.get('name' + str(i), None)
        position = request.POST.get('position'+ str(i), None)
        if position == '' : 
            position = None
        department = request.POST.get('department'+ str(i), None)
        if department == '' : 
            department = None
        phone_num = request.POST.get('phone_num' + str(i), None)
        if phone_num == '' : 
            phone_num = None
        office_num = request.POST.get('office_num'+ str(i), None)
        if office_num == '' : 
            office_num = None
        address = request.POST.get('address'+ str(i), None)
        if address == '' : 
            address = None

        if name != '':
            employee_data = Employee(name, position, department, phone_num, office_num, address) 
            employee_data.save()

    print("완료")