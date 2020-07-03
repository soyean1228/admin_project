from .models import Employee

def save(request):

    print("employee_save")

    for i in range(0,5):
        name = ''; position =''; department = ''; phone_num = ''; office_num = ''; address = ''
        name = request.POST.get('name' + str(i),'')
        position = request.POST.get('position'+ str(i),'')
        department = request.POST.get('department'+ str(i), '')
        phone_num = request.POST.get('phone_num' + str(i),'')
        office_num = request.POST.get('office_num'+ str(i),'')
        address = request.POST.get('address'+ str(i),'')
        print(name)
        if name != '' and ( position != ''  or department != ''  or phone_num != ''  or office_num != ''  or address != '' ):
            employee_data = Employee(name, position, department, phone_num, office_num, address) 
            # print("valid")
            employee_data.save()

    print("완료")