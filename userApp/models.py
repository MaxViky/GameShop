from django.conf import settings
from django.db import models

from django.contrib.auth.models import User, UserManager


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользователь', related_name='profile', on_delete=models.CASCADE)
    date_of_birth = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    photo = models.ImageField(verbose_name='Фото', upload_to='usersPhoto/', default='usersPhoto/unknownUser.jpg')

    def __str__(self):
        return 'Profile of user: {}'.format(self.user)


User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])


class friends(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', related_name='user', on_delete=models.CASCADE)
    friend = models.ForeignKey(User, verbose_name='Друг', related_name='friend', on_delete=models.CASCADE)

    def __str__(self):
        return "{0} - {1}".format(self.user, self.friend)

    class Meta:
        verbose_name = 'Друзья'
        verbose_name_plural = 'Друзья'


class Chat(models.Model):
    m_from = models.ForeignKey(User, verbose_name='Пользователь', related_name='m_from', on_delete=models.CASCADE)
    m_to = models.ForeignKey(friends, verbose_name='Друг', related_name='m_to', on_delete=models.CASCADE)
    message = models.TextField("Сообщение")

    def __str__(self):
        return "{0} - {1}".format(self.m_from, self.m_to)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'