from products.models import Access
from api.Access.serializers import AccessSerializer
from rest_framework import viewsets
from rest_framework import permissions


class AccessViewSet(viewsets.ModelViewSet):
    queryset = Access.objects.all()
    serializer_class = AccessSerializer
    permission_classes = [permissions.IsAuthenticated]

