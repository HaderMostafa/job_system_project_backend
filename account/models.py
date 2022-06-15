from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, UserManager
from .validator import validate_file_extension

from tag.models import Tag



class User(AbstractUser):
    """
    user and company model
    """
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    TYPES = (
        ('admin', 'Admin'),
        ('recruiter', 'Recruiter'),
        ('developer', 'Developer'),
    )
    GENDER = (
        ('m', 'Male'),
        ('f', 'Female'),
    )
    type = models.fields.CharField(verbose_name="User Type", choices=TYPES, max_length=10)
    allow_mail_notification = models.BooleanField(default=True)
    gender = models.fields.CharField(verbose_name="Gender", choices=GENDER, max_length=1)
    date_of_birth = models.fields.DateField(verbose_name="Date of Birth")
    """
    Fields related to Developer (user_type)
    """
    tags = models.ManyToManyField(Tag)
    cv = models.FileField(verbose_name="CV", upload_to='media', validators=[validate_file_extension],null=True, blank=True)
    """
    Fields related to Recruiter (user_type)
    """
    address = models.fields.TextField(verbose_name="Address", null=True, blank=True)
    history = models.fields.TextField(verbose_name="Company History", null=True, blank=True)
    """
    AbstractUser Fields override
    """
    email = models.EmailField(verbose_name="Email Address", unique=True, max_length=50)
    is_active = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['email', 'password','gender', 'type', 'date_of_birth']
    # objects = UserManager()

    # def create_superuser(self, email, password, **extra_fields):
    #     """Create and save a SuperUser with the given email and password."""
    #     extra_fields.setdefault('is_staff', True)
    #     extra_fields.setdefault('is_superuser', True)
    #
    #     if extra_fields.get('is_staff') is not True:
    #         raise ValueError('Superuser must have is_staff=True.')
    #     if extra_fields.get('is_superuser') is not True:
    #         raise ValueError('Superuser must have is_superuser=True.')
    #
    #     return self._create_user(email, password, **extra_fields)


    def __str__(self):
        return self.username

