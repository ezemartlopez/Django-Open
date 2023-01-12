from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurant
# Create your views here.
def create(request):
    #creacion de los elementos
    #creando el lugar
    place = Place(name = 'Lugar 1', address='Calle Demo')
    place.save()
    #creando el restaurant
    restaurant = Restaurant(place = place, number_employes = 8)
    restaurant.save()

    return HttpResponse(restaurant.place.name)