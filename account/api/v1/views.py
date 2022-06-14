from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from .serializers import SignUpSerializer, UserSerializer, UserUpdateSerializer
from account.models import User


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
        response['data'] = serializer.data['username']
        response['status'] = status.HTTP_200_OK
    else:
        response['data'] = serializer.errors
        response['status'] = status.HTTP_400_BAD_REQUEST
    return Response(**response)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_user(request, user_id):
    response = {'data': {}, 'status': status.HTTP_204_NO_CONTENT}
    try:
        user = User.objects.get(id=user_id)
        serializer = UserSerializer(user, many=False)
        response['data'] = serializer.data
        response['status'] = status.HTTP_200_OK
    except ObjectDoesNotExist:
        response['data'] = {'no content'}
        response['status'] = status.HTTP_204_NO_CONTENT
    except:
        response['data'] = {'internal server error'}
        response['status'] = status.HTTP_500_INTERNAL_SERVER_ERROR
    finally:
        return Response(**response)


@api_view(['PUT', 'PATCH'])
@authentication_classes([])
@permission_classes([])
def update_user(request, user_id):
    response = {'data': {}, 'status': status.HTTP_204_NO_CONTENT}
    user_instance = User.objects.get(id=user_id)

    if request.method == 'PUT':
        serializer = UserUpdateSerializer(instance=user_instance, data=request.data)
    else:
        serializer = UserUpdateSerializer(instance=user_instance, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        response['data'] = serializer.data['username']
        response['status'] = status.HTTP_200_OK
    else:
        response['data'] = serializer.errors
        response['status'] = status.HTTP_400_BAD_REQUEST

    return Response(**response)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_logout(request):
    request.user.auth_token.delete()
    logout(request)
    return Response('User Logged out successfully')
