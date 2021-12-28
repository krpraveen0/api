from django.contrib import admin
from api.models import Students
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=['s_no','s_name','s_course','course_fee']

admin.site.register(Students,StudentAdmin)
