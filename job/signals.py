from django.db.models.signals import m2m_changed
from django.core.mail import send_mail
from tag.models import Tag
from .models import Job
from account.models import User
from notification.models import Notification


def job_creation_action(sender, **kwargs):
    obj = kwargs.get('instance')
    print("OBJECT.ID: " + str(obj.id))
    print("OBJECT.NAME: " + str(obj.name))
    print(kwargs)
    if kwargs.get('action') == 'post_add':
        tag_set = kwargs.get("pk_set")
        tag_id = tag_set.pop()
        tag = Tag.objects.get(pk=tag_id)
        developers = User.objects.filter(tags=tag).distinct()
        print(developers)
        for developer in developers:
            # if developer.allow_mail_notification == True:
            print(developer.allow_mail_notification)
            job_message = f"New job '{obj.name}' has been posted related to your subscribed tags, Check it out!"
            id = developer.id
            notify = Notification(message=job_message, user_id=id)
            notify.save()
            print("notification saved")
            if developer.allow_mail_notification == True:
                mail = developer.email
                subject = 'New Job has been posted!'
                receivers = ['hadeermostafa.094@gmail.com', mail]
                res = send_mail(subject=subject, message=job_message, from_email='djangonotifysys@gmail.com',
                                recipient_list=receivers, fail_silently=False)
                print("Email Sent Successfully!")
            else:
                pass
        # for tag_id in kwargs.get("pk_set"):
        #     print("TAG_ID: " + str(tag_id))
        #     tag = Tag.objects.get(pk=tag_id)
        #     developers = User.objects.filter(tags=tag)
        #     # tag = tag.id
        #     print(developers)
        #     print("TAG: " + str(tag))
        #     print("TAG.ID: " + str(tag.id))
        #     print("TAG.NAME: " + str(tag.name))


m2m_changed.connect(job_creation_action, sender=Job.Tags.through)
