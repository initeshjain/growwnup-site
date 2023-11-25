from django.contrib import admin

# Register your models here.
from . models import Workshop_form, Enroll

admin.site.register(Workshop_form)
admin.site.register(Enroll)