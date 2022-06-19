from django.contrib import admin

# Register your models here.

from unit.models import (Grade, Faculty)

admin.site.register(Grade)
admin.site.register(Faculty)
