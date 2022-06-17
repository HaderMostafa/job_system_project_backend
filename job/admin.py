from django.contrib import admin
from .models import Job
# from account.models import User
@admin.register(Job)
class JobAdmin (admin.ModelAdmin):
    search_fields = ['creation_time', 'accepted_developer']
    list_filter = ('name', 'status',)
    list_display = ['name', 'description', 'status', 'update_time', 'accepted_developer','banner_image', 'creation_time', 'update_time']


    # def my_custome_function_applieddeveloper_field(self, obj):
        # my_empty_list=[]
        #
        # for User_obj in obj.User_set.all():
        #     my_empty_list.append(User_obj.username)
        #     print(User_obj.username)

        # my_empty_list=[User_obj.username for User_obj in obj.User_set.all()]

        # applied_developers = [User_obj.username for User_obj in obj.User_set.all()]
        #
        # return f"{applied_developers}"


    def has_delete_permission(self, request, obj=None):
        return False


    def has_change_permission(self, request, obj=None):
        return False

