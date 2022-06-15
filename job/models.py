from django.db import models
<<<<<<< HEAD
=======

>>>>>>> 6fff8914fbf359d753825462f5171567e18c7b5c
from account.models import User


class Job(models.Model):
    STATUS = (
        ('Open', 'Open'),
        ('Inprogress', 'Inprogress'),
        ('Finished', 'Finished'),
    )

  
    name = models.fields.CharField(verbose_name='Job Name', max_length=50)
    description = models.fields.CharField(verbose_name='Description', max_length=250)
    status = models.fields.CharField(choices=STATUS,max_length=40)
    Modification_time = models.fields.DateField(verbose_name='Modification Time')
    Tags = models.ManyToManyField('tag.tag')
    #applied_developer = models.ManyToManyField('user.user')
    #accepted_developer= models.OneToOneField('user.user')
    #banner_image =models.ImageField(upload_to='job',default='')
    applied_developer = models.ManyToManyField(User, related_name="applied_developer",null=True)
    accepted_developer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="accepted_developer", null=True)
    banner_image = models.ImageField(upload_to='job', default='cat.img')
    creation_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
