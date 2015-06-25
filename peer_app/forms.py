from models import Peer, Event
import datetime
from django import forms
from django.forms.formsets import formset_factory
from django.forms import ModelForm
from django.contrib.auth.models import User


class ContactForm(ModelForm):
    name = forms.CharField(max_length=40)
    email = forms.EmailField()
    telephone_number = forms.CharField(max_length=16)
    favorite_contact = forms.NullBooleanField()
    notes = forms.CharField(max_length=100)
    event = forms.ModelMultipleChoiceField(queryset=Event.objects.all())

    class Meta:
        model = Peer
        fields = ['name', 'email', 'telephone_number', 'favorite_contact', 'notes', 'event']
        exclude = ['']

class EventForm(ModelForm):
    name = forms.CharField(max_length=40)
    date = forms.DateField()
    create_date = forms.DateTimeField()
    author = forms.ModelMultipleChoiceField(queryset=User.objects.all())

    class Meta:
        model = Event
        fields = ['name', 'date', 'author', 'create_date']
        
    
# class ContactSearch(ModelForm):
#     class Meta:
#         model = Peer
