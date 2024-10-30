
import django.contrib.auth.models
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, reverse
from django.core.paginator import Paginator

from.models import Event, Category
import django.urls
from .forms import EventForm



# Create your views here.
def home(request):
    events = Event.objects.filter(status='published')
    categories = Category.objects.all()
    search_q = request.GET.get('search_q')
    category = request.GET.get('category')
    if search_q:
        events = events.filter(title__icontains=search_q)
    if category:
        events = events.filter(category__id=category)
    
    paginator = Paginator(events, 2)
    page_number = request.GET.get('page')
    events = paginator.get_page(page_number)

    
    context = {
        'events': events,
        'categories': categories,
        'total': Event.objects.filter(status='published').count()
        
    }
    return render(request, 'event/home.html', context)

@login_required
def create_event(request):
    category = Category.objects.all()
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            category_id = request.POST['category']
            # if not category_id:
            #     category = Category.objects.get(name='others')
            # else:
            category = Category.objects.get(id=category_id)
            event.category = category
            event.author = request.user
            event.status = 'published'
            event.save()
            return redirect('home')
        else:
            return render(request, 'event/create_form.html', {'form': form})
    return render(request, 'event/create_form.html', {'category':category,'form':form})

def event_details(request, event_id):
    event = Event.objects.get(id=event_id)
    context = {
        'event': event
    }
    return render(request, 'event/event_details.html', context)

def update_event(request, event_id):
    event = Event.objects.get(id=event_id)
    form = EventForm(instance=event)
    if request.user !=  event.author:
        return redirect('home')
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        print(form)
        # pritn(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            data = form.save(commit=False)
            data.author = request.user
            data.status = request.POST.get('status', 'published')
            data.save()
            return redirect('home')
    context = {
        'event': event,
        'form':form
    }
    return render(request, 'event/update_form.html', context)

def delete_event(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.user !=  event.author:
        return redirect('home')
    event.status = 'delete'
    event.save()
    return redirect('home')

def book_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    
    user = request.user
    if user not in event.participants.all():
        event.participants.add(user)
        return redirect(reverse('event_details', args=(event.id,)))
    else:
        return redirect(reverse('event_details', args=(event.id,)))

def cancel_booking(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    user = request.user
    
    if user in event.participants.all():
        event.participants.remove(user)
        return redirect(reverse('event_details', args=(event.id,)))
    return redirect(reverse('event_details', args=(event.id,)))


def booked_event(request):
    user = request.user
    events = Event.objects.filter(participants=user, status='published')
    search_q = request.GET.get('search_q')
    if search_q:
        events = events.filter(title__icontains = search_q)
    paginator = Paginator(events, 2)
    page_number = request.GET.get('page')
    events = paginator.get_page(page_number)

    context = {
        'events': events
    }
    return render(request, 'event/booked_event.html', context)