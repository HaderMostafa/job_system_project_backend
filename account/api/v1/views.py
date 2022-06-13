from rest_framework import status, serializers
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from rest_framework.response import Response
from .serializers import SignUpSerializer

@api_view()
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def login_again(request):
    return Response(data='HI')

@api_view(['POST'])
@permission_classes([])
def signup(request):
    response = {'data': {}, 'status': status.HTTP_400_BAD_REQUEST}

    serializer = SignUpSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        response['data'] = serializer.data
        response['status'] = status.HTTP_200_OK
    else:
        response['data'] = serializer.errors
        response['status'] = status.HTTP_400_BAD_REQUEST

    return Response(**response)



        # from account.api.v1.serializers import SignUpSerializer
        # response = {'data': {}, 'status': status.HTTP_400_BAD_REQUEST}

