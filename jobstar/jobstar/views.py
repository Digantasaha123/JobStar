from django.shortcuts import render, redirect
from JobPortalApp.models import Job_User, AddJobModel
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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
        else:
            return redirect('signupPage')
    
    return render(request, 'signup.html')

def signinPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('signinPage')
    
    return render(request, 'signin.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def AddJob(request):    
    if request.method == 'POST':
        JobTitle = request.POST.get('JobTitle')
        companyName = request.POST.get('companyName')
        companyAddress = request.POST.get('companyAddress')
        designation = request.POST.get('designation')
        description = request.POST.get('description')
        Salary = request.POST.get('Salary')
        experience = request.POST.get('experience')
        deadline = request.POST.get('deadline')
        current_user = request.user
        
        addjobdata = AddJobModel(
            JobTitle=JobTitle,
            CompanyName=companyName,
            CompanyAddress=companyAddress,
            Designation=designation,
            JobDescription=description,
            Salary=Salary,
            Experience=experience,
            Deadline=deadline,
            Created_by=current_user,   
        )
        addjobdata.save()
        return redirect('JobList')
        
    return render(request, 'Recruiter/addjob.html')

@login_required
def JobList(request):
    jobs = AddJobModel.objects.all()
    return render(request, 'joblist.html', {'jobs': jobs})

@login_required
def AppliedJob(request):
    return render(request, 'Seeker/appliedjob.html')

def logoutpage(request):
    logout(request)
    return redirect('signinPage')
