from .models import Product

def save(request):
    print("product_save")

    for i in range(0,5):
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

        if productno != '' :
            # print(productno)
            product_data = Product(productno, main_category, middle_category, sub_category, professionalism_fee_rate, 
                            potential_fee_rate, additional_fee1, additional_fee2, additional_fee3 ) 
            product_data.save()

    print("완료")