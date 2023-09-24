# from django.http import Http404

from products.models import Product
# from django.contrib.auth.models import User
from api.Product.serializers import ProductSerializer
from rest_framework import viewsets
from rest_framework import permissions


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def get_object(self):
    #     try:
    #         return User.objects.get(username=self.request.kwargs['username'])
    #     except User.DoesNotExist:
    #         raise Http404
