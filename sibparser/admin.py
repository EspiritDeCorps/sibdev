from django.contrib import admin
from .models import Site, ParsedSite

class SiteAdmin(admin.ModelAdmin):

    list_display = ('id','url')

class ParsedSiteAdmin(admin.ModelAdmin):
    fields = ['site','encoding', 'title', "h1", "successfully"]
    list_display = ('site','encoding', 'title', "h1", "successfully")

admin.site.register(Site,SiteAdmin)
admin.site.register(ParsedSite,ParsedSiteAdmin)
