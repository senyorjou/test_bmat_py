from __future__ import unicode_literals

from django.db import models


class Channel(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False,
                            primary_key=True)

    def __unicode__(self):
        return self.name


class Performer(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False,
                            primary_key=True)

    def __unicode__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False,
                             unique=True)
    performer = models.ForeignKey(Performer, to_field='name')
    length = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

    class Meta:
        unique_together = ("title", "performer")


class Play(models.Model):
    channel = models.ForeignKey(Channel, to_field='name')
    title = models.ForeignKey(Song, to_field="title")
    performer = models.ForeignKey(Performer, to_field='name')
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __unicode__(self):
        return self.title.title

    def rank(self):
        return 0

    class Meta:
        unique_together = ("channel", "start")
