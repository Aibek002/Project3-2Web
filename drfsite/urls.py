from django.contrib import admin
from django.urls import path, include

from women.views import *

urlpatterns = [
    path('', index4, name='home'),
    path('page1', index1, name='page1'),
    path('page2', index2, name='page2'),
    path('page3', index3, name='page3'),
    path('page4', index, name='page4'),


]
