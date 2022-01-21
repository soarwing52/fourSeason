from django.contrib import admin
from .models import Activity

# Register your models here.
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'due_date', 'get_leaders','get_participants', 'content', 'owner', 'get_leaders',)

admin.site.register(Activity, ActivityAdmin)