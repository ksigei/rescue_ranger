from django.contrib import admin

from .models import LostPerson, Color, EyeColor, HairColor, SkinComplexion, BodyType, Height

admin_register = [LostPerson, Color, EyeColor, HairColor, SkinComplexion, BodyType, Height]
admin.site.register(admin_register)
