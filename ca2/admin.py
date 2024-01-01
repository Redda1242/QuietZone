from django.contrib.gis import admin
from django.contrib.gis.admin import GISModelAdmin
from .models import QuietZone, Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(QuietZone)
class QuietZoneAdmin(GISModelAdmin):
    list_display = ('name', 'noise_level', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    filter_horizontal = ('tags',)


admin.site.register(Tag, TagAdmin)
