from django.urls import path

from .views import *

app_name = 'store'


urlpatterns = [
    path('products/', products, name='product'),
]
