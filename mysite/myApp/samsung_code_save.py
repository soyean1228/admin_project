from .models import SamsungCode

def save(request):

    print("samsung_code_save")

    for i in range(0,5):

        samsung_code = request.POST.get('samsung_code' + str(i), None)
        manager = request.POST.get('manager' + str(i), None)
        
        department = request.POST.get('department'+ str(i), None)
        if department == '' : 
            department = None
        phone_num = request.POST.get('phone_num'+ str(i), None)
        if phone_num == '' : 
            phone_num = None
        email = request.POST.get('email'+ str(i), None)
        if email == '' : 
            email = None

        if samsung_code != '' and manager != '' and samsung_code != None and manager != None:
            samsung_code_data = SamsungCode(samsung_code, manager, department, phone_num, email) 
            samsung_code_data.save()

    print("완료")