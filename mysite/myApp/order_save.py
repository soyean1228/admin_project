from .models import OrderData
from .models import Approval
from django.core.exceptions import ObjectDoesNotExist
from openpyxl import load_workbook
from openpyxl import Workbook
import openpyxl

def save(request):
    print("order_save")

    isSuccess = "저장에 실패했습니다"   

    oppty_num = request.POST.get('oppty_num',0)
    quote_num = request.POST.get('select_quote_num',0)
    approval_data_length = request.POST.get('approval_data_length',0)
    for i in range(0, int(approval_data_length) + 1):

        order_date = None;  order_num = None; assignment = None; 
        productno = None; buy_place = None; approval_quantity = None; order_quantity = None; 
        approval_unit = None;  approval_price = None; sales_unit = None; sales_price = None; 
        delivery_request_date = None; scheduled_delivery_date = None; recipient = None
        order_balance = None; 
        
        order_num = request.POST.get('order_num' + str(i),0)
        order_date = request.POST.get('order_date' + str(i),0)
        if order_date == '' : 
            order_date = None
        assignment = request.POST.get('assignment' + str(i),0)
        if assignment == '' : 
            assignment = None
        productno = request.POST.get('productno' + str(i),0)
        if productno == '' : 
            productno = None
        order_quantity = request.POST.get('order_quantity' + str(i),0)
        if order_quantity == '' : 
            order_quantity = None
        approval_price = request.POST.get('approval_price' + str(i),0)
        if approval_price == '' : 
            approval_price = None
        scheduled_delivery_date = request.POST.get('scheduled_delivery_date' + str(i),0)
        if scheduled_delivery_date == '' : 
            scheduled_delivery_date = None
        recipient = request.POST.get('recipient' + str(i),0)
        if recipient == '' : 
            recipient = None

        #미구현
        order_balance =0

        if order_num != '' :
            # if balance == '' : 
            #     # 입력이 안되었으면 자동으로 계산되도록 
            #     # 수량 = 승인수량 - 주문수량
            #     # balance = Approval.approval_quantity - order_quantity 
            #     try :
            #         row = Approval.objects.get(quote_num =quote_num )
            #         if order_quantity != None and row.approval_quantity != None:  
            #             print(row.approval_quantity)
            #             print(" - ")
            #             print(order_quantity)
            #             balance = row.approval_quantity - int(order_quantity)
            #         elif row.approval_quantity != None and order_quantity == None:
            #             balance = row.approval_quantity
            #         else:
            #             balance = None
            #     except ObjectDoesNotExist:
            #         print("예외")
            #         balance = None
            # OrderData_data = OrderData(order_num, oppty_num, product_model_name, order_quantity, 
            #                 order_date, quote_num, scheduled_delivery_date,assignment, recipient, 
            #                 balance) 
            # OrderData_data.save()
            data_count = OrderData.objects.filter(quote_num=quote_num, productno=productno, recipient=recipient, oppty_num=oppty_num, order_num=order_num).count()

            if data_count != 0 :
                data = OrderData.objects.get(quote_num=quote_num, productno=productno, recipient=recipient, oppty_num=oppty_num, order_num=order_num)
                data.delete()
            OrderData.objects.create(quote_num=quote_num, oppty_num=oppty_num, productno=productno, recipient=recipient, order_num=order_num,order_date=order_date,assignment=assignment,
                                    order_quantity=order_quantity, scheduled_delivery_date=scheduled_delivery_date, order_balance=order_balance )
            
            # approval의 approval_balance 구현
            approval_data = Approval.objects.filter(quote_num=quote_num)
            approval_balance = approval_data.first().approval_balance - int(order_quantity)
            approval_data.update(approval_balance=approval_balance)

        isSuccess = "저장되었습니다"  
    
    return isSuccess
    
def upload(request):
    isSuccess = "실패"
    try:
        if request.method == 'POST':
            if 'file' in request.FILES:
                wb = load_workbook(filename=request.FILES['file'].file)
                first_sheet = wb.get_sheet_names()[0]
                worksheet = wb.get_sheet_by_name(first_sheet)
                print(worksheet)
                
                for row in worksheet.iter_rows(min_row=2): # Offset for header
                    if(row[0].value == None):
                        break
                    data = OrderData()
                    data.quote_num = row[2].value
                    if Approval.objects.filter(quote_num=row[2].value).count() != 0 :
                        approval = Approval.objects.filter(quote_num=row[2].value).first()
                    
                        data.oppty_num = approval.oppty_num
                        data.productno = approval.productno
                        data.recipient = approval.recipient

                        data.order_num = row[3].value
                        data.order_date = row[0].value
                        data.assignment = None
                        data.order_quantity = row[6].value
                        if row[15].value != None:
                            employee.scheduled_delivery_date = row[15].value
                        if row[16].value != None:
                            employee.scheduled_delivery_date = row[16].value

                        if data.order_num != '' and data.order_num != None:
                            data.save()
                            isSuccess = "성공" 
    except:
        isSuccess = "실패"
    return isSuccess
