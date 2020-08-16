#main 서브앱의 urls
#서브앱의 urls는 같은 위치의 view.py의 함수로 연결을 담당 (path)
#같은 위치의 views.py를 식별 못하면 import 

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from . import views

app_name = 'myApp'

urlpatterns = [
    
    # 자동완성
    url(r'^sales_autocomplete/$', views.sales_autocomplete, name = 'sales_autocomplete'),
    url(r'^scm_autocomplete/$', views.scm_autocomplete, name = 'scm_autocomplete'),
    url(r'^samsung_code_autocomplete/$', views.samsung_code_autocomplete, name = 'samsung_code_autocomplete'),
    url(r'^employee_autocomplete/$', views.employee_autocomplete, name = 'employee_autocomplete'),
    url(r'^samsung_sales_manager_autocomplete/$', views.samsung_sales_manager_autocomplete, name = 'samsung_sales_manager_autocomplete'),
    url(r'^broker_autocomplete/$', views.broker_autocomplete, name = 'broker_autocomplete'),
    url(r'^productno_autocomplete/$', views.productno_autocomplete, name = 'productno_autocomplete'),
    url(r'^customer_name_autocomplete/$', views.customer_name_autocomplete, name = 'customer_name_autocomplete'),
    url(r'^customer_name_autocomplete_oppty_num/$', views.customer_name_autocomplete_oppty_num, name = 'customer_name_autocomplete_oppty_num'),
    url(r'^customer_name_autocomplete_oppty_num/$', views.customer_name_autocomplete_oppty_num, name = 'customer_name_autocomplete_oppty_num'),



    # path('admin/', admin.site.urls),
    path('',views.index, name = 'index'),
    path('index/',views.index, name = 'index'),
    path('insert/',views.insert, name = 'insert'),
    
    path('select/',views.select, name = 'select'),
    path('business_support_select/',views.business_support_select, name = 'business_support_select'),
    # path('select/<str:table_name>/',views.select_table, name = 'select_table'),

    # path('order_upload/',views.order_upload, name = 'order_upload'),
    path('select_result/',views.select_result, name = 'select_result'),

    path('insert/<str:table_name>/',views.insert, name = 'insert'),
    path('insert_check/<str:table_name>/', views.insert_check, name='insert_check'),

    path('upload/<str:table_name>/',views.upload, name = 'upload'),
    path('download/<str:table_name>/',views.download, name = 'download'),

    path('modify/<str:table_name>/',views.modify, name = 'modify'),
    path('modify_check/<str:table_name>/',views.modify_check, name = 'modify_check'),
    # path('get_data_for_modify/<str:table_name>/',views.get_data_for_modify, name = 'get_data_for_modify'),
    
    path('select_proposal/',views.select_proposal, name = 'select_proposal'),
    path('modify_proposal/',views.modify_proposal, name = 'modify_proposal'),

    path('signin/', views.signin, name='signin'),    
    path('signout/', views.signout, name='signout'),

    path('get_propoal_data_from_oppty/', views.get_propoal_data_from_oppty, name='get_propoal_data_from_oppty'),
    path('get_approval_data_from_select_quote_num/', views.get_approval_data_from_select_quote_num, name='get_approval_data_from_select_quote_num'),
    path('get_deposit_data_from_company_registration_number/', views.get_deposit_data_from_company_registration_number, name='get_deposit_data_from_company_registration_number'),
    path('get_data_from_select_scheduled_delivery_date/', views.get_data_from_select_scheduled_delivery_date, name='get_data_from_select_scheduled_delivery_date'),
    path('get_data_from_delivery_date/', views.get_data_from_delivery_date, name='get_data_from_delivery_date'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
