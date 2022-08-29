import pprint
from django.core.management.base import BaseCommand
from parser_hh.models import Company, City, Vacancy, Skill, Salary, Schedule,\
    Experience, Employment, Specialization
import subprocess
import json
import sys


class Command(BaseCommand):

    def handle(self, *args, **options):
        file = 'parser_hh/management/commands/parser.py'
        file_json = 'database.json'
        subprocess.run(f"python {file}", shell=True)
        with open(file_json, 'r') as database:
            data = json.load(database)

        # Vacancy.objects.all().delete()

        for key, value in data.items():
            # Добавляем Город
            if not City.objects.filter(name=value['area'][0]).exists():
                City.objects.create(name=value['area'][0])
            # Добавляем Компанию
            if not Company.objects.filter(name=value['employer'][0]).exists():
                city_id = City.objects.get(name=value['area'][0]).id
                Company.objects.create(name=value['employer'][0],
                                       city_id=city_id)
                company = Company.objects.get(name=value['employer'][0])
                if 'No data' not in value['address']:
                    company.address = value['address'][0]
                    company.save()
                if 'No data' not in value['contacts']:
                    company.contact = value['contacts'][0]
                    company.save()
            # Добавляем умения
            skills_id = []
            for skill in value['key_skills']:
                if not Skill.objects.filter(name=skill).exists():
                    Skill.objects.create(name=skill)
                skill_id = Skill.objects.get(name=skill).id
                skills_id.append(skill_id)
            # Добавляем зарплату
            data_salary = value['salary']
            if len(data_salary) > 1:
                if None in data_salary:
                    data_salary.remove(None)
                    data_salary = [str(i) for i in data_salary]
                    data_salary = ' '.join(data_salary)
            if not Salary.objects.filter(name=data_salary).exists():
                Salary.objects.create(name=data_salary)
            # Добавляем график работы
            if not Schedule.objects.filter(name=value['schedule'][0]).exists():
                Schedule.objects.create(name=value['schedule'][0])
            # Добавляем опыт
            if not Experience.objects.filter(name=value['experience'][0]).exists():
                Experience.objects.create(name=value['experience'][0])
            # Добавляем тип работы
            if not Employment.objects.filter(name=value['employment'][0]).exists():
                Employment.objects.create(name=value['employment'][0])
            # Добавляем специализацию
            specs_id = []
            for spec in value['specializations']:
                if not Specialization.objects.filter(name=spec).exists():
                    Specialization.objects.create(name=spec)
                spec_id = Specialization.objects.get(name=spec).id
                specs_id.append(spec_id)
            # Добавляем вакансию
            salary_id = Salary.objects.get(name=data_salary).id
            company_id = Company.objects.get(name=value['employer'][0]).id
            schedule_id = Schedule.objects.get(name=value['schedule'][0]).id
            experience_id = Experience.objects.get(name=value['experience'][0]).id
            employment_id = Employment.objects.get(name=value['employment'][0]).id
            if not Vacancy.objects.filter(url=value['alternate_url'][0]).exists():
                Vacancy.objects.create(name=value['name'][0],
                                       url=value['alternate_url'][0],
                                       company_id=company_id,
                                       schedule_id=schedule_id,
                                       experience_id=experience_id,
                                       employment_id=employment_id,
                                       salary_id=salary_id,
                                       role=value['professional_roles'][0])
            vacancy = Vacancy.objects.get(url=value['alternate_url'][0])
            vacancy.skill.set(skills_id)
            vacancy.specialization.set(specs_id)
            # vacancy.save()
            if value['description'][0]:
                vacancy.description = value['description'][0]
                vacancy.save()
            if value['snippet'][0]:
                vacancy.requirement = value['snippet'][0]
                vacancy.save()
            if value['snippet'][1]:
                vacancy.responsibility = value['snippet'][1]
                vacancy.save()

