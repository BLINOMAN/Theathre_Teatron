from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('афиша', views.affiche, name='affiche'),
    path('труппа_театра', views.theatre_troupe, name='theatre_troupe'),
    path('о нас', views.about, name='about'),
    path('<int:pk>', views.PlaysDetailView.as_view(), name='plays_detail')
]