from __future__ import unicode_literals
import moneyed
from djmoney.models.fields import MoneyField
from django.db import models
from django.http import Http404
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
import datetime

RELEASE_FORMATS = [
    ('cd', 'Compact Disc'),
    ('cdr', 'Compact Disc-Recordable'),
    ('digital', 'Digital'),
    ('usb', 'USB / Flash Media'),
    ('vinyl', 'Vinyl Record'),
    ('cassette', 'Cassette Tape'),
    ('other', 'Other'),
]

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
    photo = models.ImageField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True)
    biography = models.TextField(null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    bandcamp = models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    soundcloud = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    bands = models.ManyToManyField('Band', blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    deleted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Label(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    bandcamp = models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    soundcloud = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    deleted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Release(models.Model):
    title = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True)
    catalog_id = models.CharField(max_length=255, null=True, blank=True, unique=True)
    format = models.CharField(max_length=255, choices=RELEASE_FORMATS, default='cd')
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', null=True, blank=True)
    bandcamp_url = models.CharField(max_length=255, blank=True)
    bandcamp_embed = models.TextField(blank=True)
    published = models.BooleanField(default=False)
    release_date = models.DateField(default=timezone.now, null=True, blank=True)
    artists = models.ManyToManyField('Artist', blank=True)
    bands = models.ManyToManyField('Band', blank=True)
    labels = models.ManyToManyField('Label', blank=True)
    reviews = models.ManyToManyField('Review', blank=True)
    notes = models.TextField(null=True, blank=True)
    credits = models.TextField(null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    deleted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '{} - {} [{}]'.format(self.artist.name, self.title, self.label.name)

    def getBandcampEmbed(self, url):
        # cache bandcamp embed
        page = requests.get(url).content
        album_id = re.search(r'(\d{8,10}) -->$', page).group(1)

        return album_id

@python_2_unicode_compatible
class Track(models.Model):
    name = models.CharField(max_length=255)
    release = models.ForeignKey('Release', on_delete=models.DO_NOTHING, null=True, blank=True)
    length = models.DurationField(null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    deleted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Review(models.Model):
    author = models.CharField(max_length=255, null=True, blank=True)
    publication = models.CharField(max_length=255, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    deleted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.author, self.publication)
