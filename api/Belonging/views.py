from products.models import Belonging
from api.Belonging.serializers import BelongSerializer
from rest_framework import viewsets
from rest_framework import permissions


class BelongViewSet(viewsets.ModelViewSet):
    queryset = Belonging.objects.all()
    serializer_class = BelongSerializer
    permission_classes = [permissions.IsAuthenticated]

