from django.db import models

class ContactType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=254)

    contact_type = models.ForeignKey(ContactType, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"