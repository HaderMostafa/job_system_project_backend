from django.urls import path

from .views import jobs_list,job_detail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    
   
    path('list/', jobs_list, name='list'),
    path('detail/<int:id>', job_detail, name='detail'),
    
]
urlpatterns=format_suffix_patterns(urlpatterns)
