from django.shortcuts import render
from .models import Flight

# Create your views here.

# Index Page
def index(request):
    return render(request,'flights/index.html',{
        "flights":Flight.objects.all()
    })

# Passengers assigned to flight
def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    return render(request, 'flights/flight.html',{
        "flights": flight,
        "passengers": flight.passengers.all()

    })