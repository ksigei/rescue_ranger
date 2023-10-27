from django.urls import path
from . import views

urlpatterns = [
    path('lost_persons/', views.list_lost_persons, name='list_lost_persons'),
    # <a href="{% url 'list_lost_persons' %}">List Lost Persons</a>
    path('lost_persons/create/', views.create_lost_person, name='create_lost_person'),
    # <a href="{% url 'create_lost_person' %}">Create Lost Person</a>
    path('lost_persons/<int:lost_person_id>/', views.view_lost_person, name='view_lost_person'),
    path('lost_persons/<int:lost_person_id>/update/', views.update_lost_person, name='update_lost_person'),
    path('create_comment/<int:lost_person_id>/', views.create_comment, name='create_comment'),

]
