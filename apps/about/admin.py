from django.contrib import admin

from modeltranslation.admin import TranslationAdmin
from .models import About, Team, SocialLink


@admin.register(About)
class AboutAdmin(TranslationAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at')



class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 1


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at')
    inlines = [SocialLinkInline]
