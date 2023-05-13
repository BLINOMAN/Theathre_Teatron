from django.db import models

class Employee(models.Model):
    name = models.CharField("", max_length=150)
    portet = models.ImageField()
    bio = models.CharField
    # plays = models.CharField("", )
    gradues = models.CharField("", max_length=1000)

class News(models.Model):
    title = models.CharField("", max_length=170)
    logo = models.ImageField("")
    # images = models.ImageField("") - сделать многофайловость
    text = models.CharField("", max_length=5000)

class Plays(models.Model):
    title = models.CharField("", max_length=170)
    date = models.DateTimeField("", max_length=170)
    logo = models.ImageField("")
    #images = models.ImageField("") - сделать многофайловость
    stuff = models.ForeignKey(Employee, on_delete=models.CASCADE) # - сделать отсылку на множество сотрудников
    duration = models.IntegerField()
    age_limit = models.IntegerField()
    Pushkins_card = models.BooleanField()
    annotation = models.CharField("", max_length=2500)
"""
СПЕКТАКЛИ:
1. Название
2. Дата(ты)
3. Лого
4. Прочие изображения
6. Список сотрудников
7. Продолжительность
8. Стоимость
9. Возрастной ценз
10. Пушкинская карта
11. Описание
"""

"""
НОВОСТИ:
1. Название
2. Лого
3. Прочие изображения
4. Описание
"""

"""
СОТРУДНИК:
1. Имя
2. Портрет
3. Биография
4. Спектакли
5. Награды
"""