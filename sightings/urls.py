from django.urls import path
from . import views

urlpatterns = [
    path('report/', views.report_sighting, name='report_sighting'),
    path('report/success/', views.sighting_success, name='sighting_success'), 
]
