from django.urls import path
from .views import home, delete, cross_off, uncross, edit, getdata

urlpatterns = [
    path('', home, name='home'),
    path('getdata/', getdata, name='getdata'),
    path('delete/<int:list_id>/', delete, name='delete'),
    path('cross_off/<int:list_id>/', cross_off, name='cross_off'),
    path('uncross/<int:list_id>/', uncross, name='uncross'),
    path('edit/<int:list_id>/', edit, name='edit'),
]
