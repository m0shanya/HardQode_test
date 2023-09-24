from rest_framework import serializers
from products.models import Access


class AccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Access
        fields = [
            "id",
            "product",
            "user"
        ]
