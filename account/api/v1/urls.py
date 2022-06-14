from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import login_again, signup, get_users, get_user, update_user
# app_name = 'job_system_rest_v1'

urlpatterns = [
    path('rest_login/', obtain_auth_token),
    path('login_again/', login_again),
    path('signup/', signup, name='signup'),
    path('list/', get_users, name='list'),
    path('detail/<int:user_id>', get_user, name='detail'),
    path('update/<int:user_id>', update_user, name='update'),
]
