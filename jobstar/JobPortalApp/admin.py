from django.contrib import admin
from JobPortalApp.models import *

#username ta abstract, tai models e likhi nai 
class job_user_display(admin.ModelAdmin):
    list_display = ['Fullname', 'username', 'UserType']

#মডেল গুলা এইখানে রেজিস্টার করেছি
admin.site.register(Job_User, job_user_display)