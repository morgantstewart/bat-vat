from django.db import models
from django.urls import reverse
from datetime import date
# Import the User
from django.contrib.auth.models import User


# A tuple of 2-tuples added above our models
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)


class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('toy-detail', kwargs={'pk': self.id})


class Bat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    image = models.ImageField(upload_to='bats/', blank=True, null=True)

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this bat's details
        return reverse('bat-detail', kwargs={'bat_id': self.id})

    toys = models.ManyToManyField(Toy)
    # Add the foreign key linking to a user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

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

    class Meta:
        ordering = ['-date']