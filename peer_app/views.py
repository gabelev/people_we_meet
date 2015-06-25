from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from models import Event, Peer
from forms import ContactForm, EventForm
from django.contrib.auth import authenticate, login


# def index_redirect(request):
#     return render(request, )

def main_list(request):
    peer_list = Peer.objects.all()
    if request.method == 'POST':
        c_form = ContactForm(request.POST)
        if c_form.is_valid():
            peer = c_form.save(commit=False)
            peer.user = request.user
            peer.save()          
    else:
        c_form = ContactForm()

    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        people = Peer.objects.filter(name__icontains=q)
        return render(request, 'peer-search-block.html', {
            'peer_list': peer_list, 
            'c_form': c_form,
            'people': people,
            'query': q
        })

    return render(request, 'peer-list-block.html', {
        'peer_list': peer_list, 
        'c_form': c_form,
    })

def main_list_event(request):
    e_list = Event.objects.all()
    if request.method == 'POST':
        e_form = EventForm(request.POST)
        if e_form.is_valid():
            event_data = e_form.save(commit=False)
            event_data.user = request.user
            event_data.save()            
    else:
        e_form = EventForm()

    return render(request, 'event-list-block.html', {
        'e_list': e_list,
        'e_form': e_form,
    })
