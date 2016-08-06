from __future__ import unicode_literals
from django.db import models
from django.http import Http404
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
import datetime

@python_2_unicode_compatible
class Band(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    deleted = models.DateTimeField(null=True)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Artist(models.Model):
    name = models.CharField(max_length=255)
    band = models.ForeignKey('Band', on_delete=models.DO_NOTHING, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    deleted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Label(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    deleted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Release(models.Model):
    title = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True)
    published = models.BooleanField(default=False)
    published_date = models.DateField(default=timezone.now, null=True, blank=True)
    artist = models.ForeignKey('Artist', on_delete=models.DO_NOTHING, null=True, blank=True)
    band = models.ForeignKey('Band', on_delete=models.DO_NOTHING, null=True, blank=True)
    label = models.ForeignKey('Label', on_delete=models.DO_NOTHING, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    deleted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '{} - {} [{}]'.format(self.artist.name, self.title, self.label.name)

@python_2_unicode_compatible
class Track(models.Model):
    name = models.CharField(max_length=255)
    release = models.ForeignKey('Release', on_delete=models.DO_NOTHING, null=True, blank=True)
    length = models.DurationField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    deleted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.id, self.name)


