from django.contrib import admin
from .models import EventOrganizerForm

@admin.register(EventOrganizerForm)
class EventOrganizerFormAdmin(admin.ModelAdmin):
    list_display = ['event_name', 'event_start_datetime', 'event_closing_datetime', 'gate_opening_time', 'event_location', 'event_organizer_name']
    search_fields = ['event_name', 'event_location', 'event_organizer_name']

