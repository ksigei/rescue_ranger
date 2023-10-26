from django.shortcuts import render, redirect
from .forms import SightingForm

def report_sighting(request):
    if request.method == 'POST':
        form = SightingForm(request.POST, request.FILES)
        if form.is_valid():
            sighting = form.save(commit=False)
            sighting.reported_by = request.user
            sighting.save()
            # Implement notification or other logic here
            return redirect('sighting_success')  # Redirect to a success page
    else:
        form = SightingForm()
    return render(request, 'sightings/report_sighting.html', {'form': form})
