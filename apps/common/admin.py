from django.contrib import admin

from .models import Country

admin.site.site_header = 'Welcome to Global Tour Admin Panel'
admin.site.site_title = 'Global Tour Site Admin'
admin.site.index_title = 'Global Tour Admin Panel'

admin.site.register(Country)
