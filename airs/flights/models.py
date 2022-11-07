from django.db import models

# Create your models here.

# Airport Model
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"({self.code}) {self.city}"


# Flights Model
class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures')
    destination =models.ForeignKey(Airport,on_delete=models.CASCADE,related_name='arrivals')
    duration = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.origin} to {self.destination} takes {self.duration}"

# Passengers Model
class Passenger(models.Model):
    first = models.CharField(max_length=50)
    second = models.CharField(max_length=50)
    flight = models.ManyToManyField(Flight,blank=True, related_name='passengers')

def __str__(self):
    return f"{self.first} {self.second} on {self.flight}"