from django.contrib import admin

# Register your models here.
from .models import Company, City, Vacancy, Skill, Salary, Schedule,\
    Experience, Employment, Param


admin.site.register(Company)
admin.site.register(City)
admin.site.register(Vacancy)
admin.site.register(Skill)
admin.site.register(Salary)
admin.site.register(Schedule)
admin.site.register(Experience)
admin.site.register(Employment)
admin.site.register(Param)
