from rest_framework import serializers
from products.models import Lesson


class LessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = [
            "id",
            "name",
            "link",
            "duration"
        ]
