from django.contrib import admin
from .models import Subteam, HoursWorked, Student, LabHours, OverallStats

# Register your models here.

admin.site.register(Subteam)
admin.site.register(HoursWorked)
admin.site.register(Student)
admin.site.register(LabHours)
admin.site.register(OverallStats)