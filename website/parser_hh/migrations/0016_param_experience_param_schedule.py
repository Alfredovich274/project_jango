# Generated by Django 4.1 on 2022-08-29 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_hh', '0015_rename_params_param'),
    ]

    operations = [
        migrations.AddField(
            model_name='param',
            name='experience',
            field=models.CharField(blank=True, max_length=8),
        ),
        migrations.AddField(
            model_name='param',
            name='schedule',
            field=models.CharField(blank=True, max_length=8),
        ),
    ]