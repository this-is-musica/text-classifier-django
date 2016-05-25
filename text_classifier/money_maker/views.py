from django.shortcuts import render
from django.http import HttpResponse
from . import analysis


def index(request):
    return render(request, 'money_maker/index.html')
