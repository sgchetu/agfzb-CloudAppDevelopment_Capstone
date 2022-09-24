from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
# - Name
    name = models.CharField(null=False, max_length=40)
# - Description
    description = models.CharField(null=False, max_length=250)
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
    def __str__(self):
        return 'Name:' + self.name + \
            'Description:' + self.description


class CarModel(models.Model):
    id = models.IntegerField(default=1, primary_key=True)

    SEDAN = 'sedan'
    SUV = 'suv'
    WAGON = 'wagon'
    OTHERS = 'others'
    CAR_TYPES = [(SEDAN, "Sedan"), (SUV, "SUV"), (WAGON, "Wagon"), (OTHERS, "Others")]
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
    make = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
# - Name
    name = models.CharField(null=False, max_length=40)
# - Dealer id, used to refer a dealer created in cloudant database
    dealer_id = models.IntegerField(null=True)
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
    type = models.CharField(null=False, max_length=30, choices=CAR_TYPES)
# - Year (DateField)
    year = models.DateField(null=True)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
    def __str__(self):
        return 'Name ' + self.name

# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
