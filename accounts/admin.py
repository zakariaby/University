from django.contrib import admin

# Register your models here.

from accounts.models import (Student, Teacher)

admin.site.register(Teacher)
admin.site.register(Student)
