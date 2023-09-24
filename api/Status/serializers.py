from rest_framework import serializers
from products.models import Status


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            "id",
            "user",
            "lesson",
            "time",
            "status",
            "date"
        ]
