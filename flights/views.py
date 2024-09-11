
from django.shortcuts import render, redirect
from django.db.models import Avg
from .models import Flight
from .forms import FlightForm

def home(request):
    return render(request, 'flights/home.html')

def register_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_flights')
    else:
        form = FlightForm()
    return render(request, 'flights/register_flight.html', {'form': form})

def list_flights(request):
    flights = Flight.objects.all().order_by('price')
    return render(request, 'flights/list_flights.html', {'flights': flights})

def flight_statistics(request):
    national_flights = Flight.objects.filter(type='Nacional').count()
    international_flights = Flight.objects.filter(type='Internacional').count()
    avg_price_national = Flight.objects.filter(type='Nacional').aggregate(Avg('price'))['price__avg'] or 0
    return render(request, 'flights/flight_statistics.html', {
        'national_count': national_flights,
        'international_count': international_flights,
        'avg_price_national': avg_price_national
    })
