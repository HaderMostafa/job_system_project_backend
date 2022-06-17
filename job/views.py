from django.http import JsonResponse
from .models import Job
from .serializers import JobSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .permissions import IsRecruiter
from rest_framework.decorators import permission_classes


@api_view(['GET'])
def jobs_list(request, format=None):
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return JsonResponse({"jobs": serializer.data}, safe=False)


@api_view(['POST'])
@permission_classes([IsRecruiter])
def create_job(request, format=None):
    serializer = JobSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        job = serializer.save()
        job.Tags.set(request.data.get('Tags'))
        job.applied_developer.set(request.data.get('applied_developer'))
        job.accepted_developer_id = request.data.get('accepted_developer')
        job.save()
        return Response("status: Job created successfully", status.HTTP_201_CREATED)
    return Response(status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def job_detail(request, id, format=None):
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
        if job.status == 'Open':
            job.delete()
            return JsonResponse({"status": "job is deleted successfully"}, status=status.HTTP_202_ACCEPTED)
        return JsonResponse({"status": "can't delete job of status In progress or finished"}, status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['GET'])
def job_search_list(request):
    query = request.query_params.get('query')
    jobs = Job.objects.filter(Tags__in=[query])
    serializer = JobSerializer(jobs, many=True)
    return JsonResponse({"filtered jobs": serializer.data}, safe=False)


@api_view(['Get'])
def update(request, id):
    try:
        job = Job.objects.get(pk=id)
        if request.user == job.accepted_developer or request.user == job.created_by:
            if job.status == 'Inprogress':
                job.status = 'Finished'
                job.save()
                return Response("Job updated successfully", status=status.HTTP_200_OK)
            else:
                return Response("Job status should be Inprogress to be updated", status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response("You Don't Have permission to do this action", status=status.HTTP_406_NOT_ACCEPTABLE)

    except Job.DoesNotExist:
        return Response("Job doesn't exist ", status=status.HTTP_404_NOT_FOUND)

