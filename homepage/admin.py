from django.contrib import admin

from . models import Myusr,Student,Teacher
# Register your models here.

admin.site.register(Myusr)

admin.site.register(Student)

admin.site.register(Teacher)