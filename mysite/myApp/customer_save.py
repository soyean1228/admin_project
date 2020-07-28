from .models import Customer
from .models import Employee
from openpyxl import load_workbook
from openpyxl import Workbook

def save(request):
    print("customer_save")

    sales_charge_data = Employee.objects.filter(charge='INNO 영업담당')
    scm_charge_data = Employee.objects.filter(charge='INNO SCM담당')

    for i in range(0,1):
        customer_name = None; company_registration_number = None; representative = None; 
        address = None;  opening_date = None;  field1 = None; 
        field2 = None;  field3 = None;  sales_manager = None; 
        scm_manager = None;  rate = None;  

        company_registration_number = request.POST.get('company_registration_number', None)
        customer_name = request.POST.get('customer_name', None)
        if customer_name == '' : 
            customer_name = None
        representative = request.POST.get('representative', None)
        if representative == '' : 
            representative = None
        address = request.POST.get('address', None)
        if address == '' : 
            address = None
        opening_date = request.POST.get('opening_date' , None)
        if opening_date == '' : 
            opening_date = None
        field1 = request.POST.get('field1', None)
        if field1 == '' : 
            field1 = None
        field2 = request.POST.get('field2', None)
        if field2 == '' : 
            field2 = None
        field3 = request.POST.get('field3', None)
        if field3 == '' : 
            field3 = None
        purchasing_manager = request.POST.get('purchasing_manager', None)
        if purchasing_manager == '' : 
            purchasing_manager = None
        purchasing_contact_number1 = request.POST.get('purchasing_contact_number1' , None)
        if purchasing_contact_number1 == '' : 
            purchasing_contact_number1 = None
        purchasing_contact_number2 = request.POST.get('purchasing_contact_number2', None)
        if purchasing_contact_number2 == '' : 
            purchasing_contact_number2 = None
        purchasing_email = request.POST.get('purchasing_email' , None)
        if purchasing_email == '' : 
            purchasing_email = None
        settlement_manager = request.POST.get('settlement_manager' , None)
        if settlement_manager == '' : 
            settlement_manager = None
        settlement_contact_number = request.POST.get('settlement_contact_number' , None)
        if settlement_contact_number == '' : 
            settlement_contact_number = None
        settlement_email = request.POST.get('settlement_email' , None)
        if settlement_email == '' : 
            settlement_email = None
        sales_manager = request.POST.get('sales_manager', None)
        
        count_sales_charge_data = sales_charge_data.values('name').filter(name=sales_manager).count()
        print(count_sales_charge_data)
        if count_sales_charge_data == 0:
            return "영업 담당 오류"

        if sales_manager == '' : 
            sales_manager = None
        scm_manager = request.POST.get('scm_manager' , None)

        count_scm_charge_data = scm_charge_data.values('name').filter(name=scm_manager).count()
        print(count_scm_charge_data)
        if count_scm_charge_data == 0:
            return "SCM 담당 오류"

        if scm_manager == '' : 
            scm_manager = None
        rate = request.POST.get('rate' , None)
        if rate == '' : 
            rate = None

        if company_registration_number != '' :
            customer_data = Customer(customer_name, company_registration_number, representative, address, opening_date,
            field1, field2, field3, purchasing_manager, purchasing_contact_number1, purchasing_contact_number2, purchasing_email,
            settlement_manager, settlement_contact_number, settlement_email,
            sales_manager,  scm_manager, rate) 
            customer_data.save()
            isSuccess = "성공"
        else :
            isSuccess = "실패"
    return isSuccess