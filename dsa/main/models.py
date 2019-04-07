from django.db import models


class SiteStat(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    tag = models.TextField(default="direct")

    def __str__(self):
        return str(self.date) + ": " + str(self.tag)


class Property(models.Model):
    name = models.TextField(default="property1")
    value = models.TextField(default="value1")

    def __str__(self):
        return self.name + " = " +self.value

    class Meta():
        verbose_name_plural = "Properties"


class Image(models.Model):
    name = models.TextField(default="python")
    url = models.TextField(default="/static/img/courses/python.svg")

    def __str__(self):
        return self.name


class Course(models.Model):
    code = models.TextField(default="000")
    image = models.ForeignKey(Image, on_delete=models.DO_NOTHING)
    name = models.TextField(default="Python для анализа данных")
    description = models.TextField(default="С самого нуля вы будете обучаться...")
    google_forms = models.TextField(default="https://docs.google.com/forms/d/154PrmgPscbmq01MXtt2SugR8rAOgHc1Evdtt4g6cyTU")

    def __str__(self):
        return self.code + ": " + self.name

    def description_as_list(self):
        return self.description.split('<br>')


class Cohort(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()
    duration = models.TextField(default="1 месяц")
    days_and_time = models.TextField(default="Среда, Пятница с 19:00 до 22:00")
    price = models.IntegerField(default=120000)
    price_show = models.TextField(default="120 000 тенге")
    price_show_line2 = models.TextField(default="90 000 тенге при предоплате")
    show = models.BooleanField(default=False)
    url = models.TextField(default="short_url")

    def __str__(self):
        return f"{self.course.name} http://dsacademy.kz/{self.url}"


class Visitor(models.Model):
    name = models.TextField(default="ФИО")
    phone = models.TextField(default="+7",blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    tag = models.TextField(default="instagram?")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    name = models.TextField(default="ФИО")
    iin = models.TextField(max_length=15, blank=True, null=True)
    phone = models.TextField(default="+7",blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        if self.cohort is not None and self.cohort.course.name is not None:
            return self.cohort.course.name + ", " + self.name
        return self.name

