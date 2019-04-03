from django.shortcuts import render
from main.models import Cohort

# Create your views here.

def index(request):

    default_cohort = -1
    try:
        default_cohort = int(request.GET.get("show","-1"))
    except:
        pass

    return render(request, "index.html", {
        "cohorts": Cohort.objects.filter(show=True),
        "default_cohort": default_cohort,
    })