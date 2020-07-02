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
    path('employee_check/',views.employee_check, name = 'employee_check'),
    path('authority_check/',views.authority_check, name = 'authority_check'),
]
