from urllib import response
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from studentProfile.serializers import StudentSerializer
from studentProfile.models import Student
from studentProfile.services import student_service


class StudentViewSet(ModelViewSet):
    
    serializer_class = StudentSerializer
    queryset = Student.objects.all()   
    
    #  creating a student
    def create(self, request):
        
       serializer = StudentSerializer(data=request.data, context=self.get_serializer_context())
       
       serializer.is_valid(raise_exception=True)

       validated_data = serializer.validated_data
       student = student_service.add_student(**validated_data)

       if student:
           response_data = StudentSerializer(student , context=self.get_serializer_context())
           return Response(response_data.data , status=status.HTTP_201_CREATED)
       
       return Response({"message" : "Student already exist"} , status=status.HTTP_400_BAD_REQUEST)

        
    
    #  getting a list of student
    def list(self, request):
        
        students = student_service.list_students()
        serializer = StudentSerializer(students , many=True ,  context=self.get_serializer_context())
        return Response(serializer.data , status=status.HTTP_200_OK)
                    

        
    
    #  getting student by id 
      
    def retrieve(self, request, pk=None):
        
        try:
            student = student_service.get_student_byid(pk)
            serializer = StudentSerializer(student , context=self.get_serializer_context())
            return Response(serializer.data , status=status.HTTP_200_OK)
        
        except Student.DoesNotExist:
            return Response({"message" : "Student not found"} , status=status.HTTP_404_NOT_FOUND)
        
    
    def update(self, request, pk=None):
        
       serializer = StudentSerializer(data=request.data, context=self.get_serializer_context())
    
       serializer.is_valid(raise_exception=True)

       validated_data = serializer.validated_data

       try:
           
           student = student_service.update_student(pk, **validated_data)
          
       except Student.DoesNotExist:
           
          return Response({"message": "Student not found"}, status=status.HTTP_404_NOT_FOUND)


       response_data = StudentSerializer(student, context=self.get_serializer_context())
       return Response(response_data.data, status=status.HTTP_200_OK)

            
        
    #  deleting student by id
    def destroy(self, request, pk=None):
        
        deleted , _ = student_service.delete_student(pk)
        
        if deleted == 0:
            return Response({"message" : "Student not found"} , status=status.HTTP_404_NOT_FOUND)
        
        return Response({"message" : "Student succesfully deleted"} ,status=status.HTTP_200_OK)




# | HTTP Verb | Method Name             |
# | --------- | ----------------------- |
# | GET       | `list()` / `retrieve()` |
# | POST      | `create()`              |
# | PUT       | `update()`              |
# | PATCH     | `partial_update()`      |
# | DELETE    | `destroy()`             |
