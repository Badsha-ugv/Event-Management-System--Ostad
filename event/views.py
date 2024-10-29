import django.contrib.auth.models
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.core.paginator import Paginator

from.models import Event
from .forms import EventForm



# Create your views here.
def home(request):
    events = Event.objects.filter(status='published')
    search_q = request.GET.get('search_q')
    if search_q:
        events = events.filter(title__icontains=search_q)
    
    paginator = Paginator(events, 2)
    page_number = request.GET.get('page')
    events = paginator.get_page(page_number)

    context = {
        'events': events
    }
    return render(request, 'event/home.html', context)

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.status = 'published'
            event.save()
            return redirect('home')
        else:
            return render(request, 'event/create_form.html', {'form': form})
    return render(request, 'event/create_form.html')

def event_details(request, event_id):
    event = Event.objects.get(id=event_id)
    context = {
        'event': event
    }
    return render(request, 'event/event_details.html', context)