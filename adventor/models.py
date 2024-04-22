from django.db import models

class EventOrganizerForm(models.Model):
    event_name = models.CharField(max_length=200)
    event_start_datetime = models.DateTimeField()
    event_closing_datetime = models.DateTimeField()
    gate_opening_time = models.TimeField()
    event_location = models.CharField(max_length=200)
    event_organizer_name = models.CharField(max_length=200)
    event_banner_image = models.ImageField(upload_to='event_banners/')
    location_google_map_url = models.URLField()

    def __str__(self):
        return self.event_name
