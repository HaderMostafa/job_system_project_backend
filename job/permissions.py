from rest_framework.permissions import BasePermission
from .models import Job
from account.models import User


class IsRecruiter(BasePermission):
    def has_permission(self, request, view):
        if request.user.type =='recruiter':
            return True
        else:
            return False
