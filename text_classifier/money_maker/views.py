from django.shortcuts import render
from django.http import HttpResponse
from . import analysis


def index(request):
    if request.method == "POST":
        context = {"genre": analysis.classify_lyrics(request.POST.get('name',''))}
        return render(request, 'money_maker/index.html', context)
    return render(request, 'money_maker/index.html')
