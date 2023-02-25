from django.contrib import admin

from .models import Users

# Register your models here.

# Users admin
class UsersAdmin(admin.ModelAdmin):
	list_display = ('chat_id', )
	search_fields = ('chat_id',)




# Admin register
admin.site.register(Users, UsersAdmin)
