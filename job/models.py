from django.db import models

class Job(models.Model):
    STATUS = (
        ('Open', 'Open'),
        ('Inprogress', 'Inprogress'),
        ('Finished', 'Finished'),
    )

  
    name = models.fields.CharField(verbose_name='Job Name', max_length=50)
    description = models.fields.CharField(verbose_name='Description', max_length=250)
    status = models.fields.CharField(choices=STATUS,max_length=40)
    Creation_time=models.fields.DateField(verbose_name='Creation Time')
    Modification_time = models.fields.DateField(verbose_name='Modification Time')
    Tags = models.ManyToManyField('tag.tag')
    #applied_developer = models.ManyToManyField('user.user')
    #accepted_developer= models.OneToOneField('user.user')
    #banner_image =models.ImageField(upload_to='job',default='')

    

    def str(self):
        return self.name
