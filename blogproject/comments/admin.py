from django.contrib import admin
from .models import Comments
# Register your models here.


class CommentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'created_time', ]


admin.site.register(Comments, CommentsAdmin)

