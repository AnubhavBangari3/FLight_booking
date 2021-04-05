from django.shortcuts import render,redirect
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login

from django.urls import reverse

from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

from .models import *
from .forms import *

# Create your views here
def home(request):
    return render(request,"FLights/home.html")
def details(request):
    A=Airport.objects.all()
    paginator=Paginator(A,12)
    page_number=request.GET.get('page')
    try:
        page_obj=paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj=paginator.page(1)
    except EmptyPage:
        page_obj=paginator.page(paginator.num_pages)

    context={
        "A":A,
        "page_number":page_number,
        "page_obj":page_obj,
        }
    return render(request,"Flights/details.html",context)

def airport_no(request,airport_id):
    airport=Airport.objects.get(pk=airport_id)

    context={
        "airport":airport,     
        "flight":Flight.objects.all(),
        }
    return render(request,"Flights/airport_no.html",context)


def flight(request):
    flight=Flight.objects.all()
    context={
        "flight":flight,
    
        }
    return render(request,"Flights/flights.html",context)

def flight_no(request,flight_id):
    flight=Flight.objects.get(pk=flight_id)
    passengers=flight.passengers.all()

    paginator=Paginator(passengers,12)
    page_number=request.GET.get('page')
    try:
        page_obj=paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj=paginator.page(1)
    except EmptyPage:
        page_obj=paginator.page(paginator.num_pages)
    context={
        "flight":flight,
        "passengers":flight.passengers.all(),
         
        "non_passengers":Passenger.objects.exclude(flights=flight).all(),
        
        "page_number":page_number,
        "page_obj":page_obj,
        }
    return render(request,"Flights/flight_no.html",context)


def book(request,flight_id):
    if request.method == "POST":
        # Accessing the flight
        flight = Flight.objects.get(pk=flight_id)

        # Finding the passenger id from the submitted form data
        passenger_id = int(request.POST["passenger"])

        # Finding the passenger based on the id
        passenger = Passenger.objects.get(pk=passenger_id)

        # Add passenger to the flight
        passenger.flights.add(flight)

        # Redirect user to flight page
        return HttpResponseRedirect(reverse("flight_no", args=(flight.id,)))
    

def passenger_book(request):
   
    if request.method == 'POST':
        
        form=PassengerForm(request.POST)
        if form.is_valid():
            form.save()
            first=form.cleaned_data.get('first')
            last=form.cleaned_data.get('last')
            flights=form.cleaned_data.get('flights')
            return redirect('passenger_book')
        else:
            
            pass
    else:
        form=PassengerForm()
        context={
            "form":form,
            
            }
        return render(request,"Flights/passenger_book.html",context)
  
def delete(request,id):
    obj=Passenger.objects.get(pk=id)
    
    context={
        "obj":obj,
        
        }
    if request.method == "POST":
        obj.delete()
        return redirect('home')
    else:
        pass
    return render(request,"FLights/delete.html",context)


def login_view(request):
    if request.method=='POST':
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(User,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(reverse('home'))
        else:
            return render(request,"Flights/login.html")
    else:
        return render(request,"Flights/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))
def register(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
        else:
            pass
            
    else:
        form=SignUpForm()
        return render(request,"Flights/register.html",{"form":form})