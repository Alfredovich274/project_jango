# Generated by Django 4.1 on 2022-08-16 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parser_hh', '0003_role_specialization_company_contact_vacancy_snippet_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.TextField(blank=True, max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='contact',
            field=models.TextField(blank=True, max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(blank=True, max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='salary',
            name='name',
            field=models.IntegerField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(blank=True, max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='specialization',
            name='name',
            field=models.CharField(blank=True, max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='employment',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='parser_hh.employment'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='experience',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='parser_hh.experience'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='parser_hh.salary'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='schedule',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='parser_hh.schedule'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='skill',
            field=models.ManyToManyField(blank=True, to='parser_hh.skill'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='snippet',
            field=models.TextField(blank=True),
        ),
    ]
