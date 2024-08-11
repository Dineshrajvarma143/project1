from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fest1(request):
    return HttpResponse("DEEPAVALI")

# Create your views here.
def fest2(request):
    return HttpResponse("ONAM")

# Create your views here.
def fest3(request):
    return HttpResponse("KUMBAMELA")