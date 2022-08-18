from django.contrib import admin
from .models import Hallstorage, Papers, Sexambydate,Student,Hall,Invigilator,Exam, Temp,Timetable
from import_export.admin import ImportExportModelAdmin
from gather.models import Attendancestored

# Register your models here.
admin.site.register(Attendancestored)

# Register your models here.
#admin.site.register(Papers)
#admin.site.register(Student)
admin.site.register(Hall)
admin.site.register(Invigilator)
admin.site.register(Exam)
admin.site.register(Timetable)
admin.site.register(Hallstorage)
admin.site.register(Sexambydate)
admin.site.register(Temp)


@admin.register(Papers)  
class PapersAdmin(ImportExportModelAdmin):
    list_display =('pcode', 'pname', 'pcount', 'department', 'edate', 'etime',  'eid',)

@admin.register(Student)  
class StudentAdmin(ImportExportModelAdmin):
    list_display =('scode', 'sname', 'sdob', 'department', 'eid', 'pid0', 'pid1', 'pid2', 'pid3', 'pid4', 'pid5')

