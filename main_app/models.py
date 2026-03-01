from django.db import models
from datetime import date

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Coffee(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    roast = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

class Feeding(models.Model):
    date = models.DateField('Feeding Date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )
    coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE)

    # --- ADD THIS CLASS ---
    class Meta:
        ordering = ['-date'] # Orders feedings by date descending
    # ----------------------

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"