from users.views import UserViewSet, ProjectViewSet, FileViewSet
from rest_framework import routers
  
router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('project', ProjectViewSet)
router.register('file', FileViewSet)
# router.register('new-user', CreateUser, basename="new-user")