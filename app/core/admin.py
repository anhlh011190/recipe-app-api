from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUseradmin

from core import models

class UserAdmin(BaseUseradmin):
	ordering  = ["id"]
	list_display = ["email", "name"]


admin.site.register(models.User, UserAdmin)