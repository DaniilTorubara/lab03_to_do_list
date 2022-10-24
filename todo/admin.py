from django.contrib import admin

# Register your models here.

from .models import TODO

class TODOAdmin(admin.ModelAdmin):
    readonly_fields = ('creation_date',)

admin.site.register(TODO, TODOAdmin)
