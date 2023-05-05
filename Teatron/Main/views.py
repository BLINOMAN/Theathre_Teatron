from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'главная.html')


def affiche(request):
    return render(request, 'афиша.html')


def theatre_troupe(request):
    return render(request, 'труппа.html')

def about(request):
    return render(request, 'о нас.html')