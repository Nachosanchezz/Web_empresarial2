from django.contrib import admin
from .models import Link

# Register your models here.

class LinkAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Personal").exists():
            return ("key", 'name')
        else:
            return super().get_readonly_fields(request, obj)

admin.site.register(Link, LinkAdmin)