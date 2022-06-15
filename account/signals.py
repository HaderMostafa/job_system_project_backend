from django.dispatch import receiver
from django.db.models.signals import post_save

from .api.v1.views import signup
from .models import User
from django.core.mail import send_mail


@receiver(post_save, sender=User)
def account_signup_action(*args, **kwargs):
    if kwargs.get('created'):
        obj = kwargs.get('instance')
        subject = 'New User Created'
        msg = obj.history
        receivers = ['hadeermostafa.094@gmail.com']
        res = send_mail(subject=subject, message=msg, from_email='djangonotifysys@gmail.com', recipient_list=receivers)
        print(res)

