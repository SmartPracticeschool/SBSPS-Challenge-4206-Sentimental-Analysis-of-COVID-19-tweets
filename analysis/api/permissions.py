from rest_framework.permissions import BasePermission
from rest_framework.authtoken.models import Token
from analysis.models import Analysis

class IsOwner(BasePermission):
    message = "You must be the owner of this analysis"

    def has_permission(self, request, view):
        user = Token.objects.get(key=request.headers['Authorization'].split()[1]).user
        analysis_id = int(request.path.split('/')[-2])
        return Analysis.objects.get(id=analysis_id).create_by.id == user.id