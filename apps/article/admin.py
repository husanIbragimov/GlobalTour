from django.contrib import admin

from .models import Article, Comment


class CommentInline(admin.TabularInline):
    readonly_fields = ('name', 'phone_number', 'content', 'created_at')
    model = Comment
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_at', 'updated_at')
    inlines = [CommentInline]
