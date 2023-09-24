from django.contrib.auth.models import User
from rest_framework import serializers


class UserModelSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "username"
        )
        read_only_fields = ("id",)
        # extra_kwargs = {'password': {'write_only': True, 'min_length': 3}}
