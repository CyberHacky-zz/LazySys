from django.contrib import admin
from . models import Contact, User
# Register your models here.
admin.site.site_header = "LazySys - SysAgile"
admin.site.register(Contact)
admin.site.register(User)
