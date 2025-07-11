from django.urls import path, include
from rest_framework.routers import DefaultRouter
from studentProfile.views.student_view import StudentViewSet
from studentProfile.views.profile_view import ProfileVIewSet


router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='students')
router.register(r'profiles' , ProfileVIewSet, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
]


#  This will automatically generate RESTful routes for:
# list, retrieve, create, update, destroy from your ModelViewSet.

# POST http://localhost:8000/api/students/
# GET http://localhost:8000/api/students/
# GET http://localhost:8000/api/students/<id>/  read single
# PUT http://localhost:8000/api/students/<id>/
# DELETE http://localhost:8000/api/students/<id>/
