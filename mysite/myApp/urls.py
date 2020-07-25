#main 서브앱의 urls
#서브앱의 urls는 같은 위치의 view.py의 함수로 연결을 담당 (path)
#같은 위치의 views.py를 식별 못하면 import 

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'myApp'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index, name = 'select'),
    path('index/',views.index, name = 'index'),
    path('insert/',views.insert, name = 'insert'),
    path('select/',views.select, name = 'select'),
    path('select/<str:table_name>/',views.select_table, name = 'select_table'),

    path('order_upload/',views.order_upload, name = 'order_upload'),
    path('select_result/',views.select_result, name = 'select_result'),

    path('insert/<str:table_name>/',views.insert, name = 'insert'),
    path('insert_check/<str:table_name>/', views.insert_check, name='insert_check'),

    path('upload/<str:table_name>/',views.upload, name = 'upload'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)