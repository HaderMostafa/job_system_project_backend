from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import signup, get_users, get_user, update_user, user_logout
# app_name = 'job_system_rest_v1'

urlpatterns = [
    path('rest_login/', obtain_auth_token),
    # path('login_again/', login_again),
    path('signupdeveloper/', signup, name='signupAsDeveloper'),
    path('signuprecruiter/', signup, name='signupAsRecruiter'),
    path('list/', get_users, name='list'),
    path('detail/<int:user_id>/', get_user, name='detail'),
    path('update/<int:user_id>/', update_user, name='update'),
    path("logout/", user_logout, name="logout"),
]
