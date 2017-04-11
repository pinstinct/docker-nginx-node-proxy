from django.contrib import admin

from member.models import CeleryTest


class CeleryTestAdmin(admin.ModelAdmin):
    readonly_fields = (
        'created_at',
    )

admin.site.register(CeleryTest)
