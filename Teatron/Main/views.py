from django.shortcuts import render
from django.views.generic import DetailView

from .models import Employee, News, Plays


class PlaysDetailView(DetailView):
    model = Plays
    template_name = "main/plays.html"
    context_object_name = 'play'


def index(request):
    plays = Plays.objects.order_by('-date')
    news = News.objects.all()
    employee = Employee.objects.order_by('name')
    return render(request, 'main/index.html', {'plays': plays, 'news': news, 'employee': employee})


def affiche(request):
    plays = Plays.objects.order_by('-date')
    news = News.objects.all()
    employee = Employee.objects.order_by('name')
    return render(request, 'main/affiche.html', {'plays': plays, 'news': news, 'employee': employee})


def theatre_troupe(request):
    plays = Plays.objects.order_by('-date')
    news = News.objects.all()
    employee = Employee.objects.order_by('name')
    return render(request, 'main/theatre_troup.html', {'plays': plays, 'news': news, 'employee': employee})


def about(request):
    plays = Plays.objects.order_by('-date')
    news = News.objects.all()
    employee = Employee.objects.order_by('name')
    return render(request, 'main/about.html', {'plays': plays, 'news': news, 'employee': employee})
