from studentProfile.models import Student



# adding a student

def add_student(name, email):
    
    if Student.objects.filter(email=email).exists():
        return None
    
    student = Student(name=name , email=email)
    student.save()
    
    return student



#  django orm query behind the scenes
# SELECT 1 AS "a" 
# FROM "yourapp_student" 
# WHERE "yourapp_student"."email" = 'test@example.com' 
# LIMIT 1;


# listing students

def list_students():
    # print(Student.objects.all().query)
    return Student.objects.all()



# getting student by id

def get_student_byid(studentid):
    return Student.objects.get(id=studentid)


# updating student by id

def update_student(studentid , **kwargs):
    
    student = Student.objects.get(id=studentid)
    
    for key , value in kwargs.items():
        setattr(student , key , value)
        
    
    student.save()
    return student

# UPDATE "school_student"
# SET "name" = 'Ali',
#     "email" = 'ali@example.com'
# WHERE "id" = 5;


# deleting student by id


def delete_student(studentid):
    return Student.objects.filter(id=studentid).delete()



# get student profile

def get_student_profile(studentid):
    
    student = Student.objects.get(id=studentid)
    
    return student.profile

