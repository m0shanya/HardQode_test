from django.urls import include, path
from rest_framework import routers

from api.Users import views
from api.Lessons.views import LessonsViewSet
from api.Product.views import ProductsViewSet
from api.Access.views import AccessViewSet
from api.Belonging.views import BelongViewSet
from api.Status.views import StatusViewSet


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'lessons', LessonsViewSet)
router.register(r'products', ProductsViewSet)
router.register(r'access', AccessViewSet)
router.register(r'belongs', BelongViewSet)
router.register(r'status', StatusViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
