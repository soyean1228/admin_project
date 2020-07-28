from .models import Proposal
from openpyxl import load_workbook
from openpyxl import Workbook
def save(request):

    print("proposal_save")

    for i in range(0,1):

        contact_conclusion_date = None; samsung_code = None; samsung_sales_manager = None;  
        point = None;  sales_manager = None;  
        address = None; email = None; resident_registration_number = None; team = None; rate = None

        contact_conclusion_date = request.POST.get('contact_conclusion_date' + str(i), None)
        if contact_conclusion_date == '' : 
            contact_conclusion_date = None
        samsung_code = request.POST.get('samsung_code'+ str(i), None)
        if samsung_code == '' : 
            samsung_code = None
        samsung_sales_manager = request.POST.get('samsung_sales_manager'+ str(i), None)
        if samsung_sales_manager == '' : 
            samsung_sales_manager = None
        point = request.POST.get('point' + str(i), None)
        if point == '' : 
            point = None
        sales_manager = request.POST.get('sales_manager'+ str(i), None)
        if sales_manager == '' : 
            sales_manager = None
        broker = request.POST.get('broker'+ str(i), None)
        if broker == '' : 
            broker = None
        scm_manager = request.POST.get('scm_manager'+ str(i), None)
        if scm_manager == '' : 
            scm_manager = None
        customer_name = request.POST.get('customer_name'+ str(i), None)
        if customer_name == '' : 
            customer_name = None
        payment_method = request.POST.get('payment_method'+ str(i), None)
        if payment_method == '' : 
            payment_method = None
        sales_type = request.POST.get('sales_type'+ str(i), None)
        if sales_type == '' : 
            sales_type = None
        demand = request.POST.get('demand'+ str(i), None)
        if demand == '' : 
            demand = None
        billing_place = request.POST.get('billing_place'+ str(i), None)
        if billing_place == '' : 
            billing_place = None
        oppty_num = request.POST.get('oppty_num'+ str(i), None)
        if oppty_num == '' : 
            oppty_num = None
        productno = request.POST.get('productno'+ str(i), None)
        buy_place = request.POST.get('buy_place'+ str(i), None)
        if buy_place == '' : 
            buy_place = None
        decision_quantity = request.POST.get('decision_quantity'+ str(i), None)
        if decision_quantity == '' : 
            decision_quantity = None
        decision_unit = request.POST.get('decision_unit'+ str(i), None)
        if decision_unit == '' : 
            decision_unit = None
        decision_price = request.POST.get('decision_price'+ str(i), None)
        if decision_price == '' : 
            decision_price = None
        sales_unit = request.POST.get('sales_unit'+ str(i), None)
        if sales_unit == '' : 
            sales_unit = None
        sales_price = request.POST.get('sales_price'+ str(i), None)
        if sales_price == '' : 
            sales_price = None
        delivery_request_date = request.POST.get('delivery_request_date'+ str(i), None)
        if delivery_request_date == '' : 
            delivery_request_date = None
        recipient = request.POST.get('recipient'+ str(i), None)
        if recipient == '' : 
            recipient = None
        recipient_phone1 = request.POST.get('recipient_phone1'+ str(i), None)
        if recipient_phone1 == '' : 
            recipient_phone1 = None
        recipient_phone2 = request.POST.get('recipient_phone2'+ str(i), None)
        if recipient_phone2 == '' : 
            recipient_phone2 = None
        delivery_address = request.POST.get('delivery_address'+ str(i), None)
        if delivery_address == '' : 
            delivery_address = None

        if oppty_num != '' and oppty_num != None:
            proposal_data = Proposal( contact_conclusion_date, samsung_code, samsung_sales_manager, point, sales_manager, broker, scm_manager,  
                                    customer_name, payment_method, sales_type, demand, billing_place, oppty_num, productno, buy_place,  decision_quantity,
                                    decision_unit, decision_price, sales_unit, sales_price, delivery_request_date, recipient, 
                                    recipient_phone1, recipient_phone2, delivery_address) 
            proposal_data.save()
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
                employee.charge = row[11].value
                employee.passwd = row[12].value
                employee.authority = row[13].value

                if employee.name != '' and employee.name != None:
                    employee.save()
                    isSuccess = "성공"
    return isSuccess