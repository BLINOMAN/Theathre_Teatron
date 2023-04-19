from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def affiche(request):
    return render(request, 'affiche.html')


def theatre_troupe(request):
    return render(request, 'theatre_troupe.html')