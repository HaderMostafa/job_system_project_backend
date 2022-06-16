from rest_framework import serializers
from .models import Job
class JobSerializer(serializers.ModelSerializer):
    class Meta: #inner class called meta to describe data of the model
        model=Job
        fields='__all__'
        depth=1
       #we use serializers when we want to return our model to the api
