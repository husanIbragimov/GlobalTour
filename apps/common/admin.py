from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from .models import Country

admin.site.site_header = 'Welcome to Global Tour Admin Panel'
admin.site.site_title = 'Global Tour Site Admin'
admin.site.index_title = 'Global Tour Admin Panel'


class ParentCountryFilter(admin.SimpleListFilter):
    title = _('parent country')
    parameter_name = 'parent'

    def lookups(self, request, model_admin):
        list_of_parents = []
        queryset = model_admin.model.objects.filter(parent__isnull=True)
        for country in queryset:
            list_of_parents.append((str(country.id), country.name))
        return sorted(list_of_parents, key=lambda tp: tp[1])

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(parent__id=self.value())
        else:
            return queryset


def make_active(modeladmin, request, queryset):
    queryset.update(is_active=True)


make_active.short_description = _('Make active')


def make_inactive(modeladmin, request, queryset):
    queryset.update(is_active=False)


make_inactive.short_description = _('Make inactive')


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent', 'is_active', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('is_active', ParentCountryFilter)
    actions = [make_active, make_inactive]


admin.site.unregister(Group)
