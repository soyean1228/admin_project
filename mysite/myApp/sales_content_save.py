from .models import SalesContent

def save(request):
    print("sales_content_save")

    for i in range(0,5):
        sales_num = None; product_model_name =None; decision_quantity = None; 
        decision_price = None; sales_price = None; beginning_purchase = None; 
        delivery_request_date = None; recipient =  None; recipient_phone = None; 
        delivery_address = None; contact_conclusion_date = None; 

        # sales_num = request.POST.get('sales_num' + str(i),None)
        product_model_name = request.POST.get('product_model_name' + str(i),None)
        if product_model_name == '' : 
            product_model_name = None
        decision_quantity = request.POST.get('decision_quantity' + str(i),None)
        if decision_quantity == '' : 
            decision_quantity = None
        decision_price = request.POST.get('decision_price' + str(i),None)
        if decision_price == '' : 
            decision_price = None
        sales_price = request.POST.get('sales_price' + str(i),None)
        if sales_price == '' : 
            sales_price = None
        beginning_purchase = request.POST.get('beginning_purchase' + str(i),None)
        if beginning_purchase == '' : 
            beginning_purchase = None
        delivery_request_date = request.POST.get('delivery_request_date' + str(i),None)
        if delivery_request_date == '' : 
            delivery_request_date = None
        recipient = request.POST.get('recipient' + str(i),None)
        if recipient == '' : 
            recipient = None
        recipient_phone = request.POST.get('recipient_phone' + str(i),None)
        if recipient_phone == '' : 
            recipient_phone = None
        delivery_address = request.POST.get('delivery_address' + str(i),None)
        if delivery_address == '' : 
            delivery_address = None
        contact_conclusion_date = request.POST.get('contact_conclusion_date' + str(i),None)
        if contact_conclusion_date == '' : 
            contact_conclusion_date = None

        print(sales_num)

        if product_model_name != None or decision_quantity != None or decision_price != None or sales_price != None or beginning_purchase != None or delivery_request_date != None or recipient != None or recipient_phone != None or delivery_address != None or contact_conclusion_date != None :
            sales_num = SalesContent.number()
            sales_content_data = SalesContent( sales_num, product_model_name, decision_quantity, decision_price, sales_price, beginning_purchase, delivery_request_date, recipient, recipient_phone, delivery_address, contact_conclusion_date ) 
            sales_content_data.save()

    print("완료")