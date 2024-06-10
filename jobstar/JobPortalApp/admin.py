from django.contrib import admin
from JobPortalApp.models import Job_User, AddJobModel

#username ta abstract, tai models e likhi nai 
class job_user_display(admin.ModelAdmin):
    list_display = ['Fullname', 'username', 'UserType']
    
class Add_Job_List_Display(admin.ModelAdmin):
    list_display = ['JobTitle','Created_by','CompanyName']
    
    
#মডেল গুলা এইখানে রেজিস্টার করেছি
admin.site.register(Job_User, job_user_display)
admin.site.register(AddJobModel, Add_Job_List_Display)