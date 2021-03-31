from django.contrib import admin
from .models import EmployeeInfo
from .models import DailyAttendenceInfor
# Register your models here.
admin.site.register(EmployeeInfo)
admin.site.register(DailyAttendenceInfor)
