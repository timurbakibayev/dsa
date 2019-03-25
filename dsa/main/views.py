from django.shortcuts import render
from main.models import Cohort

# Create your views here.

def index(request):

    return render(request, "index.html", {"cohorts": Cohort.objects.filter(show=True)})