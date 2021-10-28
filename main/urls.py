from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name="index"),
    path('record',record,name="record"),
    path('identify',identify,name="identify")
]