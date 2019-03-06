import datetime, json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

from .models import Event, Participant
from .forms import *


# @login_required(login_url='/example url you want redirect/')
@login_required
def index(request): 
    return render(request, 'home.html')


@login_required
def allEvents(request):
    events = Event.objects.all().order_by('-id')
    context =[]
    for event in events:
        participants = Participant.objects.filter(event=event).count()
        detail = {'event':event, 'participants':participants}
        context.append(detail)
    return render(request, 'all_events.html', {'context':context, 'user':request.user})


@login_required
def createEvent(request):
    """
    """
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.created_by = request.user
            obj.save()
            return redirect('my_events')
    else:
        form = EventForm()
    return render(request, 'create-event.html', {'form':form})


@login_required
def updateEvent(request, pk):
    event = get_object_or_404(Event, pk=pk)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('my_events')
    return render(request, 'create-event.html', {'form': form})


@login_required
def deleteEvent(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method=='GET':
        event.delete()
        return redirect('my_events')
    events = Event.objects.filter(user=request.user)
    return render(request, 'myevents.html', {'event': events})


@login_required
def myEvents(request):

    events = Event.objects.filter(participants=request.user)
    return render(request, 'myevents.html', {'event':events})


def attend_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    try:
        attendee = Participant.objects.get(event=event, user=request.user)
    except:
        attendee = Participant(event=event, user=request.user)
    attendee.save()
    return redirect('all_events')


@login_required
def joinUser(request):
    pass
#     if request.is_ajax():
#         event_id = request.GET.get('envetId')
#         try:
#             events = Event.objects.get(id=event_id)
#             events.participants.add(request.user)
#             events.save()
#             context_dict = {'success': "success", 'status': 200}
#         except ObjectDoesNotExist:
#             context_dict = {'errors': "Bad Request", 'status': 400}

#     else:
#         context_dict = {'errors': "Bad Request", 'status': 400}
#     return HttpResponse(json.dumps(context_dict),content_type="application/json")
