from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet
from .models import User, Project, File
from .serializers import UserSerializer, ProjectSerializer, FileSerializer



from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import authentication, permissions
import json


   
# @api_view(('GET',))    
# def view_all_users(request):
#     user = User.objects.all()
#     serializer = UserSerializer(user, many=True)
#     return Response(serializer.data)

@api_view(('POST',))    
def create_a_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED)
    return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    
@api_view(('POST',))
@permission_classes([IsAuthenticated,])
def get_user_profile(request):
    serializer = UserSerializer()

    object = json.loads(request.body)
    username_search = object["username"]
    user_info = User.objects.filter(username=f"{username_search}").values()
    print(user_info)
    return JsonResponse({"data": list(User.objects.filter(username=f"{username_search}").values())})


class UserViewSet(ModelViewSet):
    
    permission_classes = [IsAuthenticated,]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
class FileViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    
    

# Create your views here.
