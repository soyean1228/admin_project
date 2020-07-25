from .models import Product
from openpyxl import load_workbook
from openpyxl import Workbook

def save(request):
    print("product_save")

    for i in range(0,1):
        productno = None; main_category = None; middle_category = None
        sub_category = None; professionalism_fee_rate =''; potential_fee_rate = None
        additional_fee1 = None; additional_fee2 = None; additional_fee3 = None

        productno = request.POST.get('productno' + str(i), None)
        main_category = request.POST.get('main_category' + str(i), None)
        if main_category == '' : 
            main_category = None
        middle_category = request.POST.get('middle_category' + str(i), None)
        if middle_category == '' : 
            middle_category = None
        sub_category = request.POST.get('sub_category' + str(i), None)
        if sub_category == '' : 
            sub_category = None
        professionalism_fee_rate = request.POST.get('professionalism_fee_rate' + str(i), None)
        if professionalism_fee_rate == '' : 
            professionalism_fee_rate = None
        potential_fee_rate = request.POST.get('potential_fee_rate' + str(i), None)
        if potential_fee_rate == '' : 
            potential_fee_rate = None
        additional_fee1 = request.POST.get('additional_fee1' + str(i), None)
        if additional_fee1 == '' : 
            additional_fee1 = None
        additional_fee2 = request.POST.get('additional_fee2' + str(i), None)
        if additional_fee2 == '' : 
            additional_fee2 = None
        additional_fee3 = request.POST.get('additional_fee3' + str(i), None)
        if additional_fee3 == '' : 
            additional_fee3 = None

        if productno != '':
            product_data = Product(productno, main_category, middle_category, sub_category, professionalism_fee_rate, 
                            potential_fee_rate, additional_fee1, additional_fee2, additional_fee3 ) 
            product_data.save()
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
                product = Product()
                product.productno = row[0].value
                product.main_category = row[1].value
                product.middle_category = row[2].value
                product.sub_category = row[3].value
                product.professionalism_fee_rate = row[4].value
                product.potential_fee_rate = row[5].value
                product.additional_fee1 = row[6].value
                product.additional_fee2 = row[7].value
                product.additional_fee3 = row[8].value

                if product.productno != '' and product.productno != None:
                    product.save()
                    isSuccess = "성공"
    return isSuccess