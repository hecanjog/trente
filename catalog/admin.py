from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.db.models import Count
import models
from django import forms
from django.utils.safestring import mark_safe

class AdminImageWidget(forms.FileInput):
    """
    A ImageField Widget for admin that shows a thumbnail.
    """

    def __init__(self, attrs={}):
        super(AdminImageWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        output = []
        if value and hasattr(value, "url"):
            output.append(('<a target="_blank" href="%s">'
                           '<img src="%s" style="height: 100px;" /></a> '
                           % (value.url, value.url)))
        output.append(super(AdminImageWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))

class TrackInline(admin.TabularInline):
    model = models.Track
    extra = 0

class ReleaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'release_date', 'created', 'updated', 'deleted')
    search_fields = ['title']
    change_list_template = 'smuggler/change_list.html'
    inlines = [TrackInline]
    formfield_overrides = {
        models.models.ImageField: {'widget': AdminImageWidget}
    }

class ReleaseInline(admin.StackedInline):
    model = models.Release
    extra = 0

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']
    change_list_template = 'smuggler/change_list.html'
    inlines = [ReleaseInline]

class BandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']
    change_list_template = 'smuggler/change_list.html'
    inlines = [ReleaseInline]

class TrackAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']
    change_list_template = 'smuggler/change_list.html'

admin.site.register(models.Release, ReleaseAdmin)
admin.site.register(models.Artist, ArtistAdmin)
admin.site.register(models.Band, BandAdmin)
admin.site.register(models.Track, TrackAdmin)
admin.site.register(models.Label)
