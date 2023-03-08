# the signal file lets us define signals that are fired once certain actions are taken

from django.db.models.signals import post_save
# the user model is going to be the sender, since it sends the signal.
from django.contrib.auth.models import User
# further we need to define the receiver
from django.dispatch import receiver
from .models import Profile

# the below function defines, that once a user is created, the following signal should be sent.
@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs ):
    # if the user is created, we want to create a user that is equal to the instance
    if created:
        Profile.objects.create(user = instance)


@receiver(post_save, sender = User)
def create_profile(sender, instance, **kwargs ):
    # if the user is created, we want to create a user that is equal to the instance
    instance.profile.save()
