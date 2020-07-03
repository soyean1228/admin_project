from .models import Authority

def save(request):
    print("customer_purchasing_save")

    for i in range(0,5):
        name = ''; authority =''; 
        name = request.POST.get('authority_name' + str(i),'')
        authority = request.POST.get('authority_authority' + str(i), '')
        if name != '' :
            authority_data = Authority(name, authority) 
            authority_data.save()
    print("완료")