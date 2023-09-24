from products.models import Status
from api.Status.serializers import StatusSerializer
from rest_framework import viewsets
from rest_framework import permissions


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [permissions.IsAuthenticated]

