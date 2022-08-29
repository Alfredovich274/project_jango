from django.db import models


# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=32, unique=True, blank=True)

    def __str__(self):
        return self.name


class Specialization(models.Model):
    name = models.CharField(max_length=64, unique=True, blank=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=32, unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.TextField(max_length=128, blank=True)
    contact = models.TextField(max_length=128, blank=True)

    def __str__(self):
        return self.name


class Employment(models.Model):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name


class Experience(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Salary(models.Model):
    name = models.CharField(max_length=32, unique=True, blank=True)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True)  # Описание
    # Трудоустройство
    employment = models.ForeignKey(Employment, on_delete=models.CASCADE,
                                   blank=True)
    # Опыт
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE,
                                   blank=True)
    # Зарплата
    salary = models.ForeignKey(Salary, on_delete=models.CASCADE, blank=True)
    # Тип занятости
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, blank=True)
    # Что нужно
    requirement = models.TextField(blank=True)
    # и чем придется заниматься
    responsibility = models.TextField(blank=True)
    # роли
    role = models.CharField(max_length=64, blank=True)
    # специализация
    specialization = models.ManyToManyField(Specialization, blank=True)
    url = models.CharField(max_length=64, blank=True)
    skill = models.ManyToManyField(Skill, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Param(models.Model):
    key_words = models.CharField(max_length=64)
    salary = models.CharField(max_length=8, blank=True, null=True)
    city = models.CharField(max_length=8, blank=True, null=True)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, blank=True,
                                 null=True)
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE,
                                   blank=True, null=True)

    def __str__(self):
        return self.key_words
