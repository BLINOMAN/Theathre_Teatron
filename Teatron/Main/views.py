from django.shortcuts import render
from .models import Employee, News, Plays
from django.views.generic import DetailView

# Create your views here.

plays = Plays.objects.order_by('-date')
news = News.objects.all()
employee = Employee.objects.order_by('name')

class PlaysDetailView(DetailView):
    model = Plays
    template_name = "main/спектакль.html"
    context_object_name = 'play'

def index(request):
    return render(request, 'main/главная.html', {'plays': plays,'news': news,'employee': employee})

def affiche(request):
    return render(request, 'main/афиша.html', {'plays': plays,'news': news,'employee': employee})

def theatre_troupe(request):
    return render(request, 'main/труппа.html', {'plays': plays,'news': news,'employee': employee})

def about(request):
    return render(request, 'main/о нас.html', {'plays': plays,'news': news,'employee': employee})