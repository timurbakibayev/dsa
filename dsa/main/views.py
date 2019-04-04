from django.shortcuts import render
from main.models import Cohort
from main.models import Property
from main.models import SiteStat
import pandas as pd


def index(request):
    default_cohort = -1

    site_stat = SiteStat()
    site_stat.tag = request.GET.get("tag", "direct")
    site_stat.save()

    try:
        default_cohort = int(request.GET.get("show","-1"))
    except:
        pass

    context = {
        "cohorts": Cohort.objects.filter(show=True),
        "default_cohort": default_cohort,
    }

    properties = {"consultation_google_form": ""}

    for key in properties:
        try:
            context[key] = Property.objects.get(name=key).value
        except Exception as e:
            pass

    return render(request, "index.html", context)


def stat(request):
    context = {}
    return render(request, "stats.html", context)