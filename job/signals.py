
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Job
from account.models import User
from notification.models import Notification


@receiver(post_save, sender=Job)
def job_update_action(*args, **kwargs):
    print(kwargs)
    if kwargs.get('created') == False:
        obj = kwargs.get('instance')
        job_owner = obj.created_by
        job_owner_obj = User.objects.get(username=job_owner)
        print(job_owner_obj.allow_mail_notification)
        if job_owner_obj.allow_mail_notification == True:
            subject = 'Job has been finished'
            mail = job_owner_obj.email
            receivers = ['hadeermostafa.094@gmail.com', mail]
            msg = f"Job has been marked as finished from the developer, Please check {job_owner}'s work"
            id = job_owner.id
            notify = Notification(message=msg, user_id=id)
            notify.save()
            res = send_mail(subject=subject, message=msg, from_email='djangonotifysys@gmail.com', recipient_list= receivers, fail_silently=False)
            print(res)
        else:
            pass

