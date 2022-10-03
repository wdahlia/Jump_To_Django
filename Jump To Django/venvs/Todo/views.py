from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def todo(request):
    return HttpResponse('안녕')