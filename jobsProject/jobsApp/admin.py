from django.contrib import admin
from jobsApp.models import hydjobs,punejobs,delhijobs
# Register your models here.

# To display all fields in tables

class hydjobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','job_title','eligibility',
                    'address','phone_number']

class punejobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','job_title','eligibility',
                    'address','phone_number']

class delhijobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','job_title','eligibility',
                    'address','phone_number']

admin.site.register(hydjobs,hydjobsAdmin)
admin.site.register(punejobs,punejobsAdmin)
admin.site.register(delhijobs,delhijobsAdmin)
