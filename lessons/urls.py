from django.urls import include, path
from rest_framework import routers

from api.Users import views
from api.Lessons.views import LessonsViewSet

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'lessons', LessonsViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
