from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, ProjectViewSet, FileViewSet
from . import views

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="users" )
router.register(r"projects", ProjectViewSet, basename="projects" )
router.register(r"files", FileViewSet, basename="files" )



urlpatterns = [
    # path('users/', views.view_all_users, name = 'list_users'),
    path('new-user/', views.create_a_user, name = 'create_user'),
    path('get-user-info/', views.get_user_profile, name = 'get_user_profile'),

    # path('login', views.login, name="login"),
]

urlpatterns += router.urls
# <int:pk>