from django.contrib import admin
from .models import Job
from django.utils.html import format_html
from django.utils.safestring import mark_safe


@admin.register(Job)
class JobAdmin (admin.ModelAdmin):
    list_filter = ('name', 'status',)
    # needed to add created_by/job_owner to job model then to search

    list_display = ['name', 'description', 'status', 'update_time', 'accepted_developer','banner_image', 'creation_time', 'update_time']

    # developer_name if it means applied_developer
    search_fields = ['applied_developer__username']

    # not working
    # search_fields = ['accepted_developer']
    list_display = ['name', 'description', 'status', 'creation_time', 'update_time', 'All_Tags', 'Applied_Developers', 'accepted_developer']

    def Applied_Developers(self, obj):
        if obj.applied_developer.all():
            return list(obj.applied_developer.all().values_list('username', flat=True))
        else:
            return 'NA'

    def All_Tags(self, obj):
        if obj.Tags.all():
            return list(obj.Tags.all().values_list('name', flat=True))
        else:
            return 'NA'

    # Not working
    # def get_image(self):
    #     return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.banner_image))

    # def image_tag(self, obj):
    #     return format_html('<img src="media" />'.format(obj.banner_image.url))

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

