from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import State, City, HotelAndRestaurants, Souvenir, News, TouristAttraction, Travelogue
from .forms import TravelogueForm
# Create your views here.


def index(request):
    travelogueform = TravelogueForm()
    if request.method == "GET":
        states = State.objects.all()
        news = News.objects.all()
        travelogue = Travelogue.objects.all()
        return render(request, 'irantourism/index.html', {
            'list_of_itemes': news,
            'states': states,
            'travel': travelogue,
            'form': travelogueform
        })
    elif request.method == "POST":
        submitted_form = TravelogueForm(request.POST, request.FILES)
        if submitted_form.is_valid():
            travelogue = Travelogue(
                name=submitted_form.cleaned_data['name'],
                description=submitted_form.cleaned_data['description'],
                image=submitted_form.cleaned_data['image'],
                is_visible=False)
            travelogue.save()
            return HttpResponseRedirect('/')


def show_cities(request, id):
    state = State.objects.all()
    cities = City.objects.all().filter(state=id)
    return render(request, 'irantourism/listview.html', {
        'list_of_itemes': cities,
        'states': state,
        'title': 'cities'
    })


def show_all_states(request):
    state = State.objects.all()
    return render(request, 'irantourism/listview.html', {
        'list_of_itemes': '',
        'states': state,
        'title': 'cities'
    })


def show_cities_detail(request, id):
    state = State.objects.all()
    city_tour = TouristAttraction.objects.all().filter(city=id)
    city_souv = Souvenir.objects.all().filter(city=id)
    city_hotel = HotelAndRestaurants.objects.all().filter(city=id)
    return render(request, 'irantourism/detail.html', {
        'city_tour': city_tour,
        'city_souv': city_souv,
        'city_hotel': city_hotel,
        'states': state,
        'title': 'details'
    })


def show_hotel_restaurants(request):
    hotel_and_restaurants = HotelAndRestaurants.objects.all()
    return render(request, 'irantourism/hotel_restaurant.html', {
        'hotel_and_restaurants': hotel_and_restaurants,
        'title': 'hotel_and_restaurants'
    })


def show_souvenir(request):
    souvenir = Souvenir.objects.all()
    return render(request, 'irantourism/souvenir.html', {
        'souvenir': souvenir,
        'title': 'souvenir'
    })


def show_tourist_attractions(request):
    attractions = TouristAttraction.objects.all()
    return render(request, 'irantourism/attractions.html', {
        'attractions': attractions,
        'title': 'attractions'
    })
