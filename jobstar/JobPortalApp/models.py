from django.db import models
from django.contrib.auth.models import AbstractUser

class Job_User(AbstractUser):
    [
        ('Recruiter' , 'Recruiter'),
        ('Seeker', 'Seeker')        
    ]
    Fullname = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    UserType = models.CharField(choices=USER, max_length=100)
    ProfileImage = models.ImageField(upload_to = 'static\img/')