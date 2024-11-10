from django.urls import path
from .views import *

urlpatterns = [
    path('', honey_list, name = 'honey_list'),
    path('honeys/<int:honey_id>', honey_detail, name = 'honey_detail'),
    path('about/', about, name = 'about'),
    path('contact/', contact, name = 'contact')
]