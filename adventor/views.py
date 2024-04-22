from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import EventOrganizerForm

def event_organizer_list(request):
    events = EventOrganizerForm.objects.all()
    return render(request, 'event_organizer.html', {'events': events})
