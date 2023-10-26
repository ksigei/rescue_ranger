from django.db import models

class Location(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        if self.address:
            return self.address
        elif self.city and self.state:
            return f"{self.city}, {self.state}"
        elif self.city:
            return self.city
        elif self.state:
            return self.state
        elif self.country:
            return self.country
        return "Unknown Location"
