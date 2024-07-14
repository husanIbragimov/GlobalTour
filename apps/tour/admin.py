from django.contrib import admin

from .models import Tour, TourGallery, TourPlan


class TourGalleryInline(admin.TabularInline):
    model = TourGallery
    extra = 1


class TourPlanInline(admin.TabularInline):
    model = TourPlan
    extra = 1


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_at', 'updated_at')
    inlines = [TourGalleryInline, TourPlanInline]
