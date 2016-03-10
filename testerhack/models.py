from __future__ import unicode_literals

from django.db import models

# Create your models here.


class UsersRedirect(models.Model):
    username = models.CharField(max_length=20, blank=False)
    password = models.CharField(max_length=200, blank=False)
    site = models.IntegerField(default=0)

    def __unicode__(self):
        return self.username


class SettingsUser(models.Model):
    id = models.IntegerField(default = 1, primary_key=True)
    percentage = models.IntegerField(default=50)


class AnalyticsOne(models.Model):
    id = models.IntegerField(default = 1, primary_key=True)
    visit = models.IntegerField(default=0)
    buy = models.IntegerField(default=0)


class AnalyticsTwo(models.Model):
    id = models.IntegerField(default = 1, primary_key=True)
    visit = models.IntegerField(default=0)
    buy = models.IntegerField(default=0)
