from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.

def index(request):
    # Method 1 (uncategory wise)
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))
    # params = {'number_of_slides': nSlides, 'range': range(1, nSlides), 'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #                [products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]

    #  Method 2  (category wise)
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':  allProds}
    return render(request,'shop/index2.html', params)

def about(request):
    return render(request,'shop/about.html')

def contactus(request):
    return HttpResponse('We are at ContactUs Page')

def tracker(request):
    return HttpResponse('We are at Tracker Page')

def search(request):
    return HttpResponse('We are at Search Page')

def setting(request):
    return HttpResponse('We are at Setting Page')

def productview(request):
    return HttpResponse('We are at Product View Page')

def checkout(request):
    return HttpResponse('We are at CheckOut Page')

def address(request):
    return HttpResponse('We are at Address Page')