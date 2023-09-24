from products.models import Lesson
from api.Lessons.serializers import LessonsSerializer
from rest_framework import viewsets
from rest_framework import permissions


class LessonsViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonsSerializer
    permission_classes = [permissions.IsAuthenticated]
