from django.db import models
from django.contrib.auth.models import AbstractUser
# from tag.models import Tag
# from job_system_project import tag


class User(AbstractUser):
    """
    user and company model
    """
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    TYPES = (
        ('recruiter', 'Recruiter'),
        ('developer', 'Developer'),
    )
    GENDER = (
        ('m', 'Male'),
        ('f', 'Female'),
    )
    type = models.fields.CharField(verbose_name="User Type", choices=TYPES, max_length=10, default='developer')
    allow_mail_notification = models.BooleanField(default=True)
    gender = models.fields.CharField(verbose_name="Gender", choices=GENDER, max_length=1)
    date_of_birth = models.fields.DateField(verbose_name="Date of Birth", default='2000-08-07')
    """
    Fields related to Developer (user_type)
    """
    tags = models.ManyToManyField('tag.tag')
    cv = models.FileField(verbose_name="CV", upload_to='media', null=True, blank=True)
    """
    Fields related to Recruiter (user_type)
    """
    address = models.fields.TextField(verbose_name="Address", null=True, blank=True)
    history = models.fields.TextField(verbose_name="Company History", null=True, blank=True)

    is_active = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['gender']

    def __str__(self):
        return self.username
