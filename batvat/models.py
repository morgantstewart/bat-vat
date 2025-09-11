from django.db import models
from django.urls import reverse


# A tuple of 2-tuples added above our models
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)


class Bat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this bat's details
        return reverse('bat-detail', kwargs={'bat_id': self.id})


# Add new Feeding model below Bat model
class Feeding(models.Model):
    date = models.DateField('Feeding date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )
    bat = models.ForeignKey(Bat, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"