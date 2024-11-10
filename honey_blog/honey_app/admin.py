from django.contrib import admin

from .models import Honey



class HoneyAdmin(admin.ModelAdmin):
    list_display = ('price', 'name', 'description', 'image')
    list_display_links = ('name',)
    list_filter = ( 'price', 'name')
    search_fields = ('name', 'description')
    ordering=('price','-name')
    list_editable = ('price',)
admin.site.register(Honey,HoneyAdmin)