from studentProfile.models import Student, Profile

def get_student(student_id):
    
    try:
        student  = Student.objects.get(id=student_id)
        return student
    
    except Student.DoesNotExist:
        return None
# adding a profile

def add_profile(student_id , phone , age):
    
    if Profile.objects.filter(student_id=student_id).exists():
        return None
    
    student = get_student(student_id=student_id)
    
    if not student:
        return "STUDENT_NOT_FOUND"
    
    
    profile = Profile(student=student , phone=phone , age=age)
    profile.save()
    
    return profile


# list of profiles

def list_profile():
    return Profile.objects.all()


# get profile by id

def get_profile_byid(profileid):
    return Profile.objects.get(id=profileid)



# update profile

def update_profile(profileid , **kwargs):
    
    profile = Profile.objects.get(id=profileid)
    
    for key , value in kwargs.items():
        setattr(profile, key , value)
        
    profile.save()
    
    return profile


# delete profile

def delete_profile(profileid):
    
    return Profile.objects.filter(id=profileid).delete()