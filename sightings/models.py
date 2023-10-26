from django.db import models
from accounts.models import CustomUser as User  
from lostperson.models import LostPerson  
from locations.models import Location

class Sighting(models.Model):
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    lost_person = models.ForeignKey(LostPerson, on_delete=models.CASCADE)
    sighting_location = models.ForeignKey(Location, on_delete=models.CASCADE, default=1)
    sighting_timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    contact_information = models.CharField(max_length=255)
    image = models.ImageField(upload_to='sighting_images/', blank=True, null=True)

    def __str__(self):
        return f"Sighting of {self.lost_person.name} by {self.reported_by.email}"
