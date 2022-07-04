from django.db import models

# Create your models here.


class State(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class HotelAndRestaurants(models.Model):
    HOTEL_OR_RESTAURANT = [
        ('HOTEL', 'Hotel'),
        ('RESTAURANT', 'Restaurant')
    ]
    type_of_building = models.CharField(max_length=20,
                                        choices=HOTEL_OR_RESTAURANT, default='HOTEL')
    name = models.CharField(max_length=100, null=False)
    adress = models.CharField(max_length=250, null=False)
    description = models.TextField()
    phone_num = models.CharField(max_length=11)
    image = models.ImageField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class News(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    detail = models.TextField()
    image = models.ImageField()

    def __str__(self) -> str:
        return self.title


class Souvenir(models.Model):
    name = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=11)
    description = models.TextField()
    image = models.ImageField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class TypeOfAttraction(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class TouristAttraction(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    adress = models.CharField(max_length=250, null=False)
    type_of_attraction = models.ForeignKey(
        TypeOfAttraction, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Travelogue(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    is_visible = models.BooleanField()

    def __str__(self) -> str:
        return self.name
