# Generated by Django 4.1 on 2022-08-29 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parser_hh', '0012_remove_params_experience_remove_params_schedule_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='params',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='params',
            name='schedule',
        ),
        migrations.AddField(
            model_name='params',
            name='experience',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='parser_hh.experience'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='params',
            name='schedule',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='parser_hh.schedule'),
            preserve_default=False,
        ),
    ]
