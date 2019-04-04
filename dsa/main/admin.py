from django.contrib import admin
from main.models import Image
from main.models import Course
from main.models import Cohort
from main.models import Student
from main.models import Visitor
from main.models import Property
from main.models import SiteStat

default_images = [
    {"name": "python", "url": "/static/img/courses/python.svg"},
    {"name": "machine learning", "url": "/static/img/courses/machine_learning.svg"},
    {"name": "excel", "url": "/static/img/courses/excel.svg"},
]

for img in default_images:
    if len(Image.objects.filter(name__contains=img["name"])) == 0:
        image = Image()
        image.name = img["name"]
        image.url = img["url"]
        image.save()


# Register your models here.
admin.site.register(Image)
admin.site.register(Course)
admin.site.register(Cohort)
admin.site.register(Student)
admin.site.register(Visitor)
admin.site.register(Property)
admin.site.register(SiteStat)