from rest_framework.permissions import BasePermission


class IsRecruiter(BasePermission):
    def has_permission(self, request, view):
        if request.user.type == 'recruiter':
            return True
        else:
            return False
