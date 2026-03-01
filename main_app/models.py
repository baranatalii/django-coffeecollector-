from django.db import models

class Coffee(models.Model): # <-- Check that the name is exactly 'Coffee'
    name = models.CharField(max_length=100)
    roast = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name
