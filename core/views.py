from django.shortcuts import render, HttpResponse

# Create your views here.

def soma(request, a, b):
    return HttpResponse('<h1>{} + {} = {}</h1>'.format(a, b, (a + b)))

def subt(request, a, b):
    return HttpResponse('<h1>{} - {} = {}</h1>'.format(a, b, (a - b)))

def mult(request, a, b):
    return HttpResponse('<h1>{} * {} = {}</h1>'.format(a, b, (a * b)))

def divd(request, a, b):
    return HttpResponse('<h1>{} / {} = {}</h1>'.format(a, b, (a / b)))