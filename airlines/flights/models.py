from django.db import models

# Create your models here.



# Airport Table Model
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    
    def __str__(self):
        return f'{self.city} : {self.code}'







#  Flight Table Model
class flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE,related_name='departures')
    destination =models.ForeignKey(Airport, on_delete=models.CASCADE,related_name='arrivals')
    duration = models.IntegerField()

    # Representation of the values
    def __str__(self):
        return f'from {self.origin} to {self.destination}'
    



