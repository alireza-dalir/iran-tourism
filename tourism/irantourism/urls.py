from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('cities/<int:id>', views.show_cities),
    path('all-cities', views.show_all_states),
    path('cities-detail/<int:id>', views.show_cities_detail),
    path('hotelrestaurant', views.show_hotel_restaurants),
    path('souvenir', views.show_souvenir),
    path('attractions', views.show_tourist_attractions),

]
