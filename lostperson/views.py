from django.shortcuts import render, redirect
from .models import LostPerson
from .forms import LostPersonForm

# View to create a new lost person record
def create_lost_person(request):
    if request.method == 'POST':
        form = LostPersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_lost_persons')  # Redirect to a list view
    else:
        form = LostPersonForm()
    return render(request, 'create_lost_person.html', {'form': form})

# View to update an existing lost person record
def update_lost_person(request, lost_person_id):
    lost_person = LostPerson.objects.get(id=lost_person_id)
    if request.method == 'POST':
        form = LostPersonForm(request.POST, request.FILES, instance=lost_person)
        if form.is_valid():
            form.save()
            return redirect('list_lost_persons')  # Redirect to a list view
    else:
        form = LostPersonForm(instance=lost_person)
    return render(request, 'update_lost_person.html', {'form': form, 'lost_person': lost_person})

# View to list all lost person records
def list_lost_persons(request):
    lost_persons = LostPerson.objects.all()
    return render(request, 'list_lost_persons.html', {'lost_persons': lost_persons})

# View to view details of a lost person record
def view_lost_person(request, lost_person_id):
    lost_person = LostPerson.objects.get(id=lost_person_id)
    return render(request, 'view_lost_person.html', {'lost_person': lost_person})
