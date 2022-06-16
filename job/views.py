from django.http import JsonResponse
from .models import Job
from .serializers import JobSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render


@api_view(['GET','POST'])
def jobs_list(request,fromat=None):
    #get all the drinks 
    #serialize them
    #return json
     if request.method == 'GET':
       jobs= Job.objects.all()
       serializer= JobSerializer(jobs, many=True)
       return JsonResponse({"jobs": serializer.data}, safe=False)
     if request.method == 'POST':
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        
        
@api_view(['GET', 'PUT', 'DELETE'])
def job_detail(request,id,format=None):
    try:
        job = Job.objects.get(pk=id)
    except Job.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
  
    if request.method == 'GET':
        serializer = JobSerializer(job)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = JobSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        
    elif request.method == 'DELETE':
        job.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)
