from django.contrib import admin

from .models import About, Team, SocialLink

admin.site.register(About)


class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 1


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at')
    inlines = [SocialLinkInline]
