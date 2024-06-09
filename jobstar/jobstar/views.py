from django.shortcuts import render, redirect

def signupPage(request):
    return render(request, 'signup.html')