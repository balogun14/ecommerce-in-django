from django.urls import path

from .views import *

app_name = 'store'


urlpatterns = [
    path('index/', index, name='index'),
]