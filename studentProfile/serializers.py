from rest_framework import serializers
from studentProfile.models import Student , Profile


class ProfileSerializer(serializers.ModelSerializer):

    student_id = serializers.IntegerField(write_only=True)
    student_name = serializers.CharField(source='student.name' , read_only=True)

    class Meta:
        model = Profile
        fields = ['id' , 'student_id' , 'phone' , 'age' , 'student_name']


class StudentSerializer(serializers.ModelSerializer):
    
    profile = ProfileSerializer(read_only=True)
    
    class Meta:
        model = Student
        fields = ['id' , 'name' , 'email' , 'profile']
