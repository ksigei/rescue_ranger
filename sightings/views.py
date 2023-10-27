from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Sighting
from .forms import SightingForm

def report_sighting(request):
    if request.method == 'POST':
        form = SightingForm(request.POST, request.FILES)
        if form.is_valid():
            sighting = form.save(commit=False)
            
            # if request.user.is_authenticated:
            #     sighting.reported_by = request.user
            # else:
            #     sighting.reported_by = None  

            sighting.save()
            # Implement notification or other logic here
            return redirect('sighting_success')  # Redirect to a success page
    else:
        form = SightingForm()
    return render(request, 'report_sighting.html', {'form': form})

# sighting_success
def sighting_success(request):
    return render(request, 'sighting_success.html')