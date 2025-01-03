# Generated by Django 5.0.9 on 2024-11-11 15:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClassApp', '0001_initial'),
        ('FeeApp', '0005_remove_studentfee_student'),
        ('SessionApp', '0005_sessionmaster_current_session'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentfee',
            name='class_id',
        ),
        migrations.RemoveField(
            model_name='studentfee',
            name='session',
        ),
        migrations.AddField(
            model_name='feeinvoice',
            name='class_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ClassApp.classmaster'),
        ),
        migrations.AddField(
            model_name='feeinvoice',
            name='session',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='SessionApp.sessionmaster'),
        ),
    ]
