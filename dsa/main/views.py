from django.shortcuts import render
from main.models import Cohort
from main.models import Property
from main.models import SiteStat
import pandas as pd
import os
import datetime
import matplotlib.pyplot as plt
from os.path import join
from dsa import settings

def index(request, course_name):
    print("course name", course_name)
    default_cohort = -1

    site_stat = SiteStat()
    site_stat.tag = request.GET.get("tag", "direct")
    site_stat.save()

    try:
        default_cohort = Cohort.objects.filter(show=True).filter(url=course_name)[0].id
    except:
        pass

    context = {
        "cohorts": Cohort.objects.filter(show=True),
        "default_cohort": default_cohort,
    }




    try:
        Property.objects.filter(name="any_message")[0]
    except:
        property = Property()
        property.name = "any_message"
        property.value = "Курсы рассчитаны как на опытных программистов, так и на новичков без навыков программирования"
        property.save()

    for property in Property.objects.all():
        context[property.name] = property.value

    try:
        property = Property.objects.filter(name="no_animation")[0]
    except:
        property = Property()
        property.name = "no_animation"
        property.value = "1"
        property.save()

    context["no_animation"] = property.value == "1"

    return render(request, "index.html", context)


def stat(request):
    context = {}
    dates = []
    tags = []
    for row in SiteStat.objects.all():
        dates.append(row.date)
        tags.append(row.tag)

    df = pd.DataFrame({
        "datetime": dates,
        "tag": tags,
    })

    df["date"] = df["datetime"].apply(lambda x: str(x)[:10])

    start_date = datetime.date.today() + datetime.timedelta(-30)
    end_date = datetime.date.today()

    df_date = pd.DataFrame({
        "date": pd.date_range(start_date, end_date),
    })

    df_date["count"] = df_date["date"].astype(str).apply(lambda x: len(df[df["date"] == x]))

    try:
        property = Property.objects.filter(name="stat")[0]
    except:
        property = Property()
        property.name = "stat"

    try:
        property.value = str(int(property.value)+1)
    except:
        property.value = "1"

    property.save()

    filename = f"stat{property.value}.png"

    figure = plt.figure(figsize=(15,10))

    old_files = join(settings.MEDIA_ROOT, "*.png")

    os.system(f"rm {old_files}")
    # print(old_files)

    path = join(settings.MEDIA_ROOT, filename)
    context["files"] = []

    context["files"].append(f"/media/{filename}")
    plt.clf()
    plt.plot(df_date["date"],df_date["count"])
    plt.title("Visits by dates")
    plt.savefig(path)

    k = 0
    for i in df["tag"].unique():
        k += 1
        df_date = pd.DataFrame({
            "date": pd.date_range(start_date, end_date),
        })
        df1 = df[df["tag"] == i]

        df_date["count"] = df_date["date"].astype(str).apply(lambda x: len(df1[df1["date"] == x]))
        filename = f"{k}_{property.value}.png"
        context["files"].append(f"/media/{filename}")
        plt.clf()
        plt.plot(df_date["date"],df_date["count"])
        plt.title(i)
        path = join(settings.MEDIA_ROOT, filename)
        plt.savefig(path)

    print(df.head(10))
    print(df_date.tail(10))


    return render(request, "stats.html", context)
