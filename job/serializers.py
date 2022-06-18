from rest_framework import serializers
from .models import Job
class JobSerializer(serializers.ModelSerializer):
    class Meta: #inner class called meta to describe data of the model
        model=Job
        fields=['id','name','description','status','creation_time','Modification_time','Tags']
        
       #we use serializers when we want to retuen our model to the api
