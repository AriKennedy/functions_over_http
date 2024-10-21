from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest

# Create your views here.
def hey_you(request, name):
    return HttpResponse(f"Hey, {name}!")

def how_old(request, end, birthyear):
    age = int(end) - int(birthyear)
    return HttpResponse(age)

def canITakeYourOrder(request, burgers, fries, drinks):
    total = (int(burgers) * 4.50) + (int(fries) * 1.50) + (int(drinks) * 1.00)
    return HttpResponse(total)