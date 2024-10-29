from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("event/create/", views.create_event, name="create_event"),
    path("event/<int:event_id>/", views.event_details, name="event_details"),
]
