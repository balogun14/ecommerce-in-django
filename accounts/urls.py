from django.urls import path

from .views import *
app_name = 'accounts'
urlpatterns = [
    path('index/', index, name='index'),
    path("login/", login, name="login")
]
