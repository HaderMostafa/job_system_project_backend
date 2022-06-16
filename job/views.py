from django.shortcuts import render
from rest_framework import generics
from django.http import JsonResponse
from .models import Job
from .serializers import JobSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .permissions import IsRecruiter
from rest_framework.decorators import permission_classes

@api_view(['GET','POST'])
# @permission_classes([IsRecruiter])
def jobs_list(request,format=None):
     if request.method=='GET':
       jobs=Job.objects.all()
       serializer=JobSerializer(jobs,many=True)
       return JsonResponse({"jobs":serializer.data},safe=False)
     if request.method=='POST':
        #print('////////////////////////////')
        # print(request.data.get('applied_developer')[0].get('id'))
        serializer= JobSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            job = serializer.save()
            job.Tags.set(request.data.get('Tags'))
            job.applied_developer.set(request.data.get('applied_developer'))
            job.accepted_developer_id = request.data.get('accepted_developer')
            job.save()
            return Response("status: Job created successfully",status.HTTP_201_CREATED)
        return Response(status.HTTP_400_BAD_REQUEST)
        
        
@api_view(['GET','PUT','DELETE'])
def job_detail(request,id,format=None):
    try:
     job= Job.objects.get(pk=id)
    except Job.DoesNotExist:
     return Response(status=status.HTTP_404_NOT_FOUND)
  
    if request.method=='GET':
        serializer=JobSerializer(job)
        return Response(serializer.data) 
    elif request.method=='PUT':
        serializer= JobSerializer(job,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        
    elif request.method=='DELETE':
         if job.status=='Open':
           job.delete()
           return JsonResponse({"status":"job is deleted successfully"},status=status.HTTP_202_ACCEPTED)
         return JsonResponse({"status":"can't delete job of status In progress or finished"},status=status.HTTP_404_NOT_FOUND)
        
@api_view(['GET'])
def job_search_list(request):
    query = request.query_params.get('query')
    jobs=Job.objects.filter(Tags__in=[query])
    serializer=JobSerializer(jobs,many=True)
    return JsonResponse({"filtered jobs":serializer.data},safe=False)