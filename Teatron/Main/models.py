from django.db import models


class Plays(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField("Название спектакля", max_length=170)
    date = models.DateTimeField("Дата", max_length=170)
    logo = models.ImageField("Постер", upload_to='images/', blank=True, null=True)
    duration = models.IntegerField("Длительность спектакля (в мин)")
    age_limit = models.IntegerField("Возрастное ограничение")
    Pushkins_card = models.BooleanField("Доступна ли Пушкинская карта")
    annotation = models.CharField("Аннотация к спектаклю", max_length=2500)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Спектакль"
        verbose_name_plural = "Спектакли"


class Employee(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField("Имя сотрудника", max_length=150)
    photo = models.ImageField('Портрет', upload_to='images/', blank=True, null=True)
    biography = models.CharField("Биография", max_length=1000, null=True)
    gradues = models.CharField("Награды", max_length=1000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


class Employee_group(models.Model):
    id_plays = models.ForeignKey(Plays, on_delete=models.CASCADE)
    id_employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return "Спектакль " + str(self.id_plays) + ". Сотрудник " + str(self.id_employee)

    class Meta:
        verbose_name = "Группа сотрудников"
        verbose_name_plural = "Группы сотрудников"


class News(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField("Название новости", max_length=170)
    logo = models.ImageField('Постер', upload_to='images/', blank=True, null=True)
    text = models.CharField("Текст", max_length=5000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


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
