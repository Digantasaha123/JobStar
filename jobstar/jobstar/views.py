from django.shortcuts import render, redirect
from JobPortalApp.models import Job_User

def signupPage(request):
    if request.method == 'Post':
        username = request.POST.get('username')
        fullName = request.POST.get('fullName')
        email = request.POST.get('email')
        address = request.POST.get('address')
        password = request.POST.get('password')
        confpassword = request.POST.get('confpassword')
        profileimage = request.FILES.GET('profileImage')
        userType = request.POST.get('userType')
        if password == confpassword:
            user = Job_User.objects.create(username=username, password=password)
            user.Fullname = fullName
            user.Address = address
            user.UserType = userType
            user.ProfileImage = profileimage
            user.save()
            return redirect('signinPage')
        else :
            return redirect('signupPage')
    
    return render(request, 'signup.html')

def signinPage(request):
    return render(request, 'signin.html')