from django.db import models

from .managers import ArtistManager, AlbumManager, TrackManager


class Artist(models.Model):
    name = models.CharField(max_length=255)

    objects = ArtistManager()

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=255)
    artists = models.ManyToManyField(Artist)
    release_date = models.DateField()
    purchase_date = models.DateField()
    rating = models.IntegerField()

    objects = AlbumManager()

    def __str__(self):
        return self.name


class Track(models.Model):
    title = models.CharField(max_length=255)
    album = models.ForeignKey(Album)
    rating = models.IntegerField()
    listens = models.IntegerField()

    objects = TrackManager()

    def __str__(self):
        return self.title

