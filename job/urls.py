from django.urls import path

from .views import jobs_list,job_detail,job_search_list
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    
   
    path('list', jobs_list, name='list'),
    path('detail/<int:id>', job_detail, name='detail'),
    path('filtered/',job_search_list, name='filtered')
    
]
urlpatterns=format_suffix_patterns(urlpatterns)
