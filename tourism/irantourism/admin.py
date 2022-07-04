from django.contrib import admin

from .models import State, Souvenir, HotelAndRestaurants, TouristAttraction, Travelogue, TypeOfAttraction, City, News
# Register your models here.

admin.site.register(State)
admin.site.register(Souvenir)
admin.site.register(HotelAndRestaurants)
admin.site.register(TouristAttraction)
admin.site.register(Travelogue)
admin.site.register(TypeOfAttraction)
admin.site.register(City)
admin.site.register(News)
