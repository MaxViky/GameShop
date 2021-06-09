from django.contrib.auth.models import User
from django.db import models


class Publisher(models.Model):
    name = models.CharField("Название", max_length=50)
    poster = models.ImageField('Постер', null=True, blank=True, upload_to='PublisherPoster/')
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Издатель'
        verbose_name_plural = 'Издатели'


class Developer(models.Model):
    name = models.CharField("Название", max_length=50)
    poster = models.ImageField('Постер', null=True, blank=True, upload_to='DeveloperPoster/')
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Разработчик'
        verbose_name_plural = 'Разработчики'


class Game(models.Model):
    name = models.CharField("Название", max_length=50)
    description = models.TextField('Описание')
    price = models.FloatField("Цена", default=0)
    publisher = models.ForeignKey(Publisher, verbose_name="Издатель", blank=True, max_length=50, on_delete=models.DO_NOTHING)
    developer = models.ForeignKey(Developer, verbose_name="Разработчик", blank=True, max_length=50, on_delete=models.DO_NOTHING)
    rating = models.IntegerField("Рейтинг")
    release = models.DateField("Дата релиза")
    poster = models.ImageField('Постер', null=True, upload_to='gamePoster/')
    count_download = models.IntegerField("Количество скачиваний")
    demandsOS = models.CharField('ОС', blank=True, max_length=150)
    demandsCPU = models.CharField('Процессор', blank=True, max_length=150)
    demandsRAM = models.CharField('Оперативная память', blank=True, max_length=150)
    demandsGPU = models.CharField('Видеокарта', blank=True, max_length=150)
    demandsROM = models.CharField('Место на диске', blank=True, max_length=150)
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'


class GameShots(models.Model):
    title = models.CharField("Заголовок", max_length=50)
    image = models.ImageField('Изображение', null=True, upload_to='GameShots/')
    game = models.ForeignKey(Game, verbose_name='Игра', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Скриншот'
        verbose_name_plural = 'Скриншоты'


class GameLabel(models.Model):
    name = models.CharField("Метка", max_length=50)
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Метка'
        verbose_name_plural = 'Метки'


class Tagged(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    label = models.ForeignKey(GameLabel, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} - {1}".format(self.label, self.game)

    class Meta:
        verbose_name = 'Метка к игре'
        verbose_name_plural = 'Метки к играм'


class Reviews(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', max_length=50, on_delete=models.CASCADE)
    text = models.TextField('Отзыв')
    star = models.PositiveSmallIntegerField('Оценка')
    game = models.ForeignKey(Game, verbose_name='Игра', on_delete=models.CASCADE)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Cart(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', max_length=50, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, verbose_name='Игра', on_delete=models.CASCADE)

    def __str__(self):
        return "{0} - {1}".format(self.user, self.game)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class GameLibrary(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', max_length=50, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, verbose_name='Игра', on_delete=models.CASCADE)

    def __str__(self):
        return "{0} - {1}".format(self.user, self.game)

    class Meta:
        verbose_name = 'Библиотека'
        verbose_name_plural = 'Библиотеки'


class HistoryPay(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', max_length=50, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, default=None, verbose_name='Игра', on_delete=models.CASCADE)
    datePay = models.DateTimeField("Дата покупки")

    def __str__(self):
        return "Дата:{0} \n{1}".format(self.datePay, self.game)

    class Meta:
        verbose_name = 'История покупок'
        verbose_name_plural = 'Истории покупок'