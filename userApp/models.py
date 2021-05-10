from django.conf import settings
from django.db import models

from django.contrib.auth.models import User, UserManager


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='usersPhoto/', default='usersPhoto/unknownUser.jpg')

    def __str__(self):
        return 'Profile of user: {}'.format(self.user)


User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])
