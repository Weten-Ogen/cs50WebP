from django.shortcuts import render
from .models import flight

# Create your views here.

# Index Page
def index(request):
    return render(request, 'flights/index.html', {
        'flights': flight.objects.all()
    })

