from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.

def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products.html', context)
