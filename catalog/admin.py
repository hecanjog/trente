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

class ReleaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'published', 'published_date', 'created', 'updated', 'deleted')
    formfield_overrides = {
        models.models.ImageField: {'widget': AdminImageWidget }
    }
    #inlines = [EmailInline, PhoneInline, AddressInline]
    #search_fields = ['first_name', 'last_name', 'member_id']

admin.site.register(models.Release, ReleaseAdmin)
admin.site.register(models.Artist)
admin.site.register(models.Band)
admin.site.register(models.Label)
