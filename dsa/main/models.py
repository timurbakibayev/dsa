from django.db import models


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

    def __str__(self):
        return self.code + ": " + self.name


class Cohort(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()
    duration = models.TextField(default="1 месяц")
    days_and_time = models.TextField(default="Среда, Пятница с 19:00 до 22:00")
    price = models.IntegerField(default=120000)
    price_show = models.TextField(default="120 000 тенге<br>90 000 тенге при предоплате")
    show = models.BooleanField(default=False)

    def __str__(self):
        return self.course.name + " " + str(self.start) + ", " + str(self.days_and_time)


class Visitor(models.Model):
    name = models.TextField(default="ФИО")
    phone = models.TextField(default="+7",blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    tag = models.TextField(default="instagram?")
    date = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    date = models.DateTimeField(auto_created=True)
    name = models.TextField(default="ФИО")
    iin = models.TextField(max_length=15, blank=True, null=True)
    phone = models.TextField(default="+7",blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        if self.cohort is not None and self.cohort.course.name is not None:
            return self.cohort.course.name + ", " + self.name
        return self.name

