from django.contrib.auth.models import User
from django.db.models.signals import post_save

from userApp.models import Profile


def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        up = Profile(user=user, stuff=1, thing=2)
        up.save()

post_save.connect(create_profile, sender=User)