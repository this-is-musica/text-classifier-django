from django.shortcuts import render
from django.http import HttpResponse
from . import analysis


def index(request):
    if request.method == "POST":
        return display_genre(request,analysis.classify_lyrics(request.POST.get('name','')))
    return render(request, 'money_maker/index.html')


def test(request):
    if request.method == "POST":
        return HttpResponse(analysis.classify_lyrics(request.POST.get('lyrics','')))
    else:
        return render(request, 'money_maker/lyrics_in.html')

def display_genre(request, genre):
    context = {"genre": genre}
    return render(request, 'money_maker/index.html', context)
