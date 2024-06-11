"""
URL configuration for jobstar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
##added manually * 2 
from django.conf import settings
from django.conf.urls.static import static
from jobstar.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signupPage',signupPage, name = "signupPage"),
    path('dashboard/',dashboard, name = "dashboard"),
    path('',signinPage, name = "signinPage"),
    path('profile /', profile, name = 'profile'),
    path('AddJob/', AddJob, name = 'AddJob'),
    path('AppliedJob/', AppliedJob, name = 'AppliedJob'),
    path('AppliedJob/', AppliedJob, name = 'AppliedJob'),
    path('JobList/', JobList, name = 'JobList'),
    path('logoutpage/', logoutpage, name = 'logoutpage'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
