from django.contrib import admin

from user_detail.models import ActivityModel,UserDetail
# Register your models here.

class ActivityModelAdmin(admin.ModelAdmin):
    list_display=["user","start_time","end_time"]
    list_filter=["user"]

admin.site.register(ActivityModel,ActivityModelAdmin)
admin.site.register(UserDetail)