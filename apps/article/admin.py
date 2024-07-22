from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Article, Comment


class CommentInline(admin.TabularInline):
    readonly_fields = ('name', 'phone_number', 'content', 'created_at')
    model = Comment
    extra = 0


@admin.register(Article)
class ArticleAdmin(TranslationAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'slug')
    prepopulated_fields = {
        # 'slug': ('name',),
        'slug_uz': ('name_uz',),
        'slug_ru': ('name_ru',),
        'slug_en': ('name_en',),
    }
    readonly_fields = ('created_at', 'updated_at')
    inlines = [CommentInline]


admin.site.register(Comment)
