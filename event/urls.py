from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("event/create/", views.create_event, name="create_event"),
    path("event/<int:event_id>/", views.event_details, name="event_details"),
    path("event/<int:event_id>/update/", views.update_event, name="update_event"),
    path("event/<int:event_id>/delete/", views.delete_event, name="delete_event"),
    path("event/<int:event_id>/book/", views.book_event, name="book_event"),
    path("event/<int:event_id>/book/cancel", views.cancel_booking, name="cancel_booking"),

    path('event/my_event', views.booked_event, name='booked_event'),
    

]
