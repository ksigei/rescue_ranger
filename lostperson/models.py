from django.db import models
from accounts.models import CustomUser as User

class LostPerson(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    reported_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='lost_persons/', blank=True, null=True)
    is_found = models.BooleanField(default=False)
    found_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='found_by')
    found_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-reported_at']

