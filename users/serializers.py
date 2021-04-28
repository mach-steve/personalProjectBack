from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from .models import User, Project, File
from django.contrib.auth.hashers import make_password


        
class UserSerializer(serializers.ModelSerializer):
    files_user = serializers.PrimaryKeyRelatedField(queryset=File.objects.all(), many=True)
    projects = PrimaryKeyRelatedField(queryset=Project.objects.all(), many=True)
    
    # password = serializers.CharField(
    #     write_only=True,
    #     required=True,
    #     help_text='Leave empty if no change needed',
    #     style={'input_type': 'password', 'placeholder': 'Password'}
    # )
    
    # To hash the password upon saving to the db
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)
    
    
    
    class Meta:
        model = User
        fields = ['id','username', 'password', 'email', 'first_name', 'last_name', 'sc', 'od', 'projects', 'files_user']

        
class ProjectSerializer(serializers.ModelSerializer):
    files_project = serializers.PrimaryKeyRelatedField(queryset=File.objects.all(), many=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=False)

    class Meta:
        model = Project
        fields = ['id', 'proj_name', 'user']
        
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'file', 'file_name', 'user']
        
        
        
