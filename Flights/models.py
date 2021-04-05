from django.db import models
from .forms import *
from django.forms import ModelForm
# Create your models here.
#for Flights
class Airport(models.Model):
    code=models.CharField(max_length=3)
    city=models.CharField(max_length=120)

    def __str__(self):
        return f"({self.code}) {self.city}"

class Flight(models.Model):
    origin=models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="departures")
    destination=models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="arrivals")
    duration=models.IntegerField()

    def __str__(self):
        return f"{self.id}:{self.origin} to {self.destination}"
            

class Passenger(models.Model):
    first=models.CharField(max_length=64)
    last=models.CharField(max_length=64)
    flights=models.ManyToManyField(Flight,blank=True,related_name="passengers")
    def __str__(self):
        return f"{self.first} {self.last}"



class PassengerForm(ModelForm):
    first=forms.CharField(max_length=120)
    last=forms.CharField(max_length=120)
    flights=forms.ModelMultipleChoiceField(
       queryset=Flight.objects.all(),
                                  widget=forms.CheckboxSelectMultiple)
    class Meta:
        model=Passenger
        fields=['first','last','flights']