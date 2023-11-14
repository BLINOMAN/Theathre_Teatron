from django.db import models


class Employee(models.Model):
    name = models.CharField("", max_length=150)
    portet = models.ImageField('Портрет', upload_to='images/', blank=True, null=True)
    bio = models.CharField
    gradues = models.CharField("", max_length=1000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


class News(models.Model):
    title = models.CharField("", max_length=170)
    logo = models.ImageField('Постер', upload_to='images/', blank=True, null=True)
    text = models.CharField("", max_length=5000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Plays(models.Model):
    title = models.CharField("", max_length=170)
    date = models.DateTimeField("", max_length=170)
    logo = models.ImageField("")
    stuff = models.ForeignKey(Employee, on_delete=models.CASCADE)  # - сделать отсылку на множество сотрудников
    duration = models.IntegerField()
    age_limit = models.IntegerField()
    Pushkins_card = models.BooleanField()
    annotation = models.CharField("", max_length=2500)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Спектакль"
        verbose_name_plural = "Спектакли"


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
