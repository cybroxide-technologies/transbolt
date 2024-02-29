from django.contrib import admin
from .models import UserData

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  list_display = ("userId","firstName", "lastName", "phone_number" )
admin.site.register(UserData , MemberAdmin)


