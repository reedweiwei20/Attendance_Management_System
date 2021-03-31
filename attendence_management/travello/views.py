from django.shortcuts import render
from .models import Destination
# Create your views here.
def travello(request):
    dests = Destination.objects.all()
    return render(request, 'index.html', {'dests':dests})