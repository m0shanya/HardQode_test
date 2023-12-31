from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from api.Users.serializers import UserModelSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserModelSerializer
    permission_classes = [permissions.IsAuthenticated]
