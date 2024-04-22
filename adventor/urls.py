from django.urls import path
from .views import event_organizer_list

urlpatterns = [
    path('event-list/', event_organizer_list, name='event_list'),
]
