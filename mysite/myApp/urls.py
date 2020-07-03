#main 서브앱의 urls
#서브앱의 urls는 같은 위치의 view.py의 함수로 연결을 담당 (path)
#같은 위치의 views.py를 식별 못하면 import 

from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'myApp'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index, name = 'index'),
    path('insert/',views.insert, name = 'insert'),
    path('select/',views.select, name = 'select'),
    
    # path('employee_check/',views.employee_check, name = 'employee_check'),
    # path('authority_check/',views.authority_check, name = 'authority_check'),

    # path('employee_insert/',views.employee_insert, name = 'employee_insert'),
    # path('authority_insert/',views.authority_insert, name = 'authority_insert'),
    # path('product_insert/',views.product_insert, name = 'product_insert'),
    # path('customer_insert/',views.customer_insert, name = 'customer_insert'),

    path('insert/<str:table_name>/',views.insert, name = 'insert'),

    path('insert_check/<str:table_name>/', views.insert_check, name='insert_check')
]
