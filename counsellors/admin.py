from django.contrib import admin
from .models import Counsellor

class CounsellorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    search_fields = ('id', 'name', 'email')

admin.site.register(Counsellor, CounsellorAdmin)
