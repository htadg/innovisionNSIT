from __future__ import unicode_literals

from django.db import models

# Create your models here.


class UsersRedirect(models.Model):
    username = models.CharField(max_length=20, blank=False)
    password = models.CharField(max_length=200, blank=False)
    site = models.IntegerField(default=0)

    def __unicode__(self):
        return self.username


class Settings(models.Model):
    percentage = models.IntegerField(default=50)
    org_site = models.URLField()
    new_site = models.URLField()


class AnalyticsOne(models.Model):
    hit = models.IntegerField(default=0)
    buy = models.IntegerField(default=0)


class AnalyticsTwo(models.Model):
    hit = models.IntegerField(default=0)
    buy = models.IntegerField(default=0)
