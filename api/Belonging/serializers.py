from rest_framework import serializers
from products.models import Belonging


class BelongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Belonging
        fields = [
            "id",
            "lesson",
            "product"
        ]
