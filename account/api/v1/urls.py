from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import login_again
from .views import signup

# app_name = 'job_system_rest_v1'

urlpatterns = [
    path('rest_login/', obtain_auth_token),
    path('login_again/', login_again),
    path('signup', signup, name='signup')

]
