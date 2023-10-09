from django.urls import path
# from . import views
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('delete/<list_id>',delete, name='delete'),
    path('cross_off/<list_id>',cross_off, name='cross_off'),
    path('uncross/<list_id>',uncross, name='uncross'),
    path('edit/<list_id>',edit, name='edit'),
]