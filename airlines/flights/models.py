from django.db import models

# Create your models here.



# Airport Model
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.city}'


#  Flight  Model
class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE,related_name='departures')
    destination =models.ForeignKey(Airport, on_delete=models.CASCADE,related_name='arrivals')
    duration = models.IntegerField()

    # Representation of the values
    def __str__(self):
        return f'{self.origin} {self.destination}'
    
# Passengers Model
class Passengers(models.Model):
    first = models.CharField(max_length=32)
    last = models.CharField(max_length=32)
    flights= models.ManyToManyField(Flight, blank=True,related_name="passengers")

    # Return representation
    def __str__(self):
        return f"{self.first} {self.last}"
