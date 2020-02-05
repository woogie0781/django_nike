from django.shortcuts import render

def index(request):
    return render(request, 'App/index.html', {})

def product(request):
    return render(request, 'App/product.html', {})