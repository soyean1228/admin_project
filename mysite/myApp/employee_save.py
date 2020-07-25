from .models import Employee
from openpyxl import load_workbook
from openpyxl import Workbook
def save(request):

    print("employee_save")

    for i in range(0,1):

        name = None; position = None; department = None;  phone_num = None;  office_num = None;  
        address = None; email = None; resident_registration_number = None; team = None; rate = None

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
        email = request.POST.get('email'+ str(i), None)
        if email == '' : 
            email = None
        resident_registration_number = request.POST.get('resident_registration_number'+ str(i), None)
        if resident_registration_number == '' : 
            resident_registration_number = None
        team = request.POST.get('team'+ str(i), None)
        if team == '' : 
            team = None
        rate = request.POST.get('rate'+ str(i), None)
        if rate == '' : 
            rate = None

        if name != '' and name != None:
            employee_data = Employee(name, team, position, department, resident_registration_number, rate, phone_num, office_num, address, email) 
            employee_data.save()
            isSuccess = "성공"
        else :
            isSuccess = "실패"
    return isSuccess

def upload(request):
    isSuccess = "실패"
    if request.method == 'POST':
        if 'file' in request.FILES:
            wb = load_workbook(filename=request.FILES['file'].file)
            first_sheet = wb.get_sheet_names()[0]
            worksheet = wb.get_sheet_by_name(first_sheet)
            print(worksheet)
            
            for row in worksheet.iter_rows(min_row=2): # Offset for header
                employee = Employee()
                employee.name = row[0].value
                employee.team = row[1].value
                employee.position = row[2].value
                employee.department = row[3].value
                employee.resident_registration_number = row[4].value
                employee.rate = row[5].value
                employee.phone_num = row[6].value
                employee.office_num = row[7].value
                employee.recipient = row[8].value
                employee.address = row[9].value
                employee.email = row[10].value

                if employee.name != '' and employee.name != None:
                    employee.save()
                    isSuccess = "성공"
    return isSuccess