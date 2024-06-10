from django.db import models
from django.contrib.auth.models import AbstractUser

class Job_User(AbstractUser):
    USER =  [
        ('Recruiter' , 'Recruiter'),
        ('Seeker', 'Seeker')
        ]
    Fullname = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    UserType = models.CharField(choices=USER, max_length=100)
    ProfileImage = models.ImageField(upload_to = 'static\img/')
    
class AddJobModel(models.Model):
    JobTitle = models.CharField(max_length=100,null=True)
    CompanyName = models.CharField(max_length=100,null=True)
    CompanyAddress = models.CharField(max_length=100,null=True)
    Designation = models.CharField(max_length=100,null=True)
    JobDescription = models.TextField(null = True)
    Salary = models.CharField(max_length=100,null=True)
    Experience =models.CharField(max_length=100,null=True)
    Deadline = models.CharField(max_length=100,null=True)   
    Created_by = models.ForeignKey(Job_User, on_delete=models.CASCADE)
    