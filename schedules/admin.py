from django.contrib import admin

from .models import PasswordOperator, Schedule

# Register your models here.
admin.site.register(PasswordOperator)
admin.site.register(Schedule)
