import folium as folium
from django.shortcuts import render, redirect
import requests

from . import support_functions
from .models import City
from .form import CityForm


# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=c6653f6c9abb06e0a3dd17d64a2e8145'

    cities = City.objects.all()  # return all the cities in the database
    if request.method == 'POST':  # only true if form is submitted
        form = CityForm(request.POST)  # add actual request data to form for processing
        form.save()  # will validate and save if validate
    form = CityForm()
    weather_data = []

    for city in cities:
        city_weather = requests.get(
            url.format(city)).json()  # request the API data and convert the JSON to Python data types

        weather = {
            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }
        weather_data.append(weather)  # add the data for the current city into our list

    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'index.html', context)  # returns the index.html template


def map(request):
    m = folium.Map()  # add import folium at the top of views.py
    data = dict()
    try:
        request.GET['reset']
        print("resetting")
        data['number_of_cities'] = 0
        data['m'] = m._repr_html_
        return render(request, "map.html", context=data)
    except:
        pass
    try:
        request.GET['city_list']
        number_of_cities = int(request.GET['number_of_cities'])
        visiting_cities = list()
        for i in range(number_of_cities):
            name = "city" + str(i)
            city_name = request.GET[name]
            visiting_cities.append(city_name)
        m = support_functions.add_markers(m, visiting_cities)
        data['visiting_cities'] = visiting_cities
        m = m._repr_html_
        data['m'] = m
        return render(request, "map.html", data)
    except:
        pass
    try:
        number_of_cities = int(request.GET["number_of_cities"])
        if number_of_cities > 0:
            names = list()
            for i in range(number_of_cities):
                names.append("city" + str(i))
            data['names'] = names
            data['number_of_cities'] = number_of_cities
        m = m._repr_html_
        data['m'] = m
    except:
        data['number_of_cities'] = 0
        m = m._repr_html_
        data['m'] = m
    return render(request, "map.html", context=data)


def home(request):
    return render(request, "home.html")

def index_2(request):

    return render(request, "index.html")

def delete_city(request, city_id):
    City.objects.filter(id=city_id).delete()
    return redirect('home')

