from .models import Authority

def save(request):
    print("authority_save")

    for i in range(0,5):
        name = None; authority = None; 

        name = request.POST.get('authority_name' + str(i), None)
        authority = request.POST.get('authority_authority' + str(i), None)
        if authority == '' : 
            authority = None

        if name != '' :
            authority_data = Authority(name, authority) 
            authority_data.save()
            
    print("완료")