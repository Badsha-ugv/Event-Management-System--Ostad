from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from.models import Event
from .forms import EventForm



# Create your views here.
def home(request):
    return render(request, 'event/home.html')

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('home')
        else:
            return render(request, 'event/create_form.html', {'form': form})
    return render(request, 'event/create_form.html')
