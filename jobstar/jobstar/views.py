from django.shortcuts import render, redirect
from JobPortalApp.models import Job_User
from django.contrib.auth import authenticate, login, logout

def signupPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        fullName = request.POST.get('fullName')
        email = request.POST.get('email')
        address = request.POST.get('address')
        password = request.POST.get('password')
        confpassword = request.POST.get('confpassword')
        profileimage = request.FILES.get('profileImage')
        userType = request.POST.get('userType')
        if password == confpassword:
            user = Job_User.objects.create_user(username=username, password=password)
            user.Fullname = fullName
            user.Address = address
            user.UserType = userType
            user.ProfileImage = profileimage
            user.userType = userType
            user.save() 
            return redirect('signinPage')
        else :
            return redirect('signupPage')
    
    return render(request, 'signup.html')
def signinPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username = username, password = password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else :
            return redirect('signinPage')
    
    return render(request, 'signin.html')

def dashboard(request):
    
    return render(request, 'dashboard.html')

def profile(request):
    return render(request, 'profile.html')

def AddJob(request):
    return render(request, 'Recruiter/addjob.html')


def JobList(request):
    return render(request, 'joblist.html')

def AppliedJob(request):
    return render(request, 'Seeker/appliedjob.html')