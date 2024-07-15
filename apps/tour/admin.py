from django.contrib import admin

from .models import Tour, TourGallery, TourPlan, BookingTour


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


@admin.register(BookingTour)
class BookingTourAdmin(admin.ModelAdmin):
    list_filter = ('status', 'created_at')
    readonly_fields = ('tour', 'full_name', 'phone_number', 'people', 'message', 'created_at')
    list_display = ('id', 'full_name', 'phone_number', 'tour', 'people', 'status', 'created_at')
    list_display_links = ('id', 'full_name', 'tour')
