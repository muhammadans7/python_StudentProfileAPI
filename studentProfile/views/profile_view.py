from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from studentProfile import serializers
from studentProfile.serializers import ProfileSerializer
from studentProfile.models import Student , Profile
from studentProfile.services import profile_service

class ProfileVIewSet(ModelViewSet):
    
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    
    
    def create(self, request):
        
        serializer = ProfileSerializer(data=request.data , context=self.get_serializer_context())
        
        serializer.is_valid(raise_exception=True)
        
        validated_data = serializer.validated_data
        profile = profile_service.add_profile(**validated_data)
        
        if profile == "STUDENT_NOT_FOUND":
            return Response({"message" : "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        
        if profile:
            response_data = ProfileSerializer(profile, context=self.get_serializer_context())
            return Response(response_data.data , status=status.HTTP_201_CREATED)
        
      
        
        return Response({"message" : "This Profile already belongs to a student"} ,status=status.HTTP_400_BAD_REQUEST)
    
    
    def list(self, request):
        
        profiles = profile_service.list_profile()
        serializer = ProfileSerializer(profiles , many=True, context=self.get_serializer_context())
        return Response(serializer.data , status=status.HTTP_200_OK)
    
    def retrieve(self , request , pk=None):
        
        try:
            
            profile = profile_service.get_profile_byid(pk)
            serializer = ProfileSerializer(profile , context=self.get_serializer_context())
            return Response(serializer.data , status=status.HTTP_200_OK)
        
        except Profile.DoesNotExist:
            return Response({"message" : "Profile not found"} , status=status.HTTP_404_NOT_FOUND)
        
        
        
    def update(self, request , pk=None):
        
        serializer = ProfileSerializer(data=request.data , context=self.get_serializer_context())
        
        serializer.is_valid(raise_exception=True)
        
        validated_data = serializer.validated_data
        
        try:
            profile = profile_service.update_profile(pk,**validated_data)
            response_data = ProfileSerializer(profile , context=self.get_serializer_context())
            return Response(response_data.data , status=status.HTTP_200_OK)
        
        except Profile.DoesNotExist:
            return Response({"message" : "Profile not found"} , status=status.HTTP_404_NOT_FOUND)
        
        
    def destroy(self, request , pk=None):
        
        deleted ,_ = profile_service.delete_profile(pk)
        
        if deleted == 0:
            return Response({"message" : "Profile not found"} , status=status.HTTP_404_NOT_FOUND)
        
        return Response({"message" : "Profile deleted succesfully"} , status=status.HTTP_200_OK)
