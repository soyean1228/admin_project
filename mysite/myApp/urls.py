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
    path('index/',views.index, name = 'index'),
    path('insert/',views.insert, name = 'insert'),
    path('select/',views.select, name = 'select'),
    path('select_result/',views.select_result, name = 'select_result'),

    path('insert/<str:table_name>/',views.insert, name = 'insert'),

    path('insert_check/<str:table_name>/', views.insert_check, name='insert_check')
]
