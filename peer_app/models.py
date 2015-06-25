from django.db import models
import datetime
from django.contrib.auth.models import User


class Event(models.Model):
    name = models.CharField(max_length=40)
    date = models.DateField()
    create_date = models.DateTimeField(default=datetime.datetime.now)
    author = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Peer(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(blank=True)
    telephone_number = models.CharField(max_length=16, blank=True)
    favorite_contact = models.NullBooleanField(null=True, blank=True)
    notes = models.CharField(max_length=100, blank=True)
    event = models.ManyToManyField(Event)
    # pub_date = models.DateTimeField(default=datetime.datetime.now)
    # author = models.ForeignKey(User, related_name='peer')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
    
