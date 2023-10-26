from django.db import models
from accounts.models import CustomUser as User
from locations.models import Location

class Color(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name 
class EyeColor(models.Model):
    color = models.ForeignKey(Color, on_delete=models.CASCADE)

    def __str__(self):
        return self.color.name

class HairColor(models.Model):
    color = models.ForeignKey(Color, on_delete=models.CASCADE)

    def __str__(self):
        return self.color.name
 
class SkinComplexion(models.Model):
    color = models.ForeignKey(Color, on_delete=models.CASCADE)

    def __str__(self):
        return self.color.name
    
class BodyType(models.Model):
    body_type = models.CharField(max_length=30)

    def __str__(self):
        return self.body_type
    
class Height(models.Model):
    measurement = models.CharField(max_length=30)

    def __str__(self):
        return self.measurement

class LostPerson(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default=1)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    reported_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='lost_persons/', blank=True, null=True)
    is_found = models.BooleanField(default=False)
    found_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='found_by')
    found_at = models.DateTimeField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    eye_color = models.ForeignKey(EyeColor, on_delete=models.CASCADE, blank=True, null=True)
    hair_color = models.ForeignKey(HairColor, on_delete=models.CASCADE, blank=True, null=True)
    skin_complexion = models.ForeignKey(SkinComplexion, on_delete=models.CASCADE, blank=True, null=True)
    body_type = models.ForeignKey(BodyType, on_delete=models.CASCADE, blank=True, null=True)
    height = models.ForeignKey(Height, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-reported_at']


    


     

