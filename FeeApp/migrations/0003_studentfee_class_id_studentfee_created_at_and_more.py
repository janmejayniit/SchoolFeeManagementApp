# Generated by Django 5.0.9 on 2024-11-05 09:18

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClassApp', '0001_initial'),
        ('FeeApp', '0002_studentfee'),
        ('SessionApp', '0005_sessionmaster_current_session'),
        ('StudentApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentfee',
            name='class_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ClassApp.classmaster'),
        ),
        migrations.AddField(
            model_name='studentfee',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='studentfee',
            name='session',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='SessionApp.sessionmaster'),
        ),
        migrations.AlterField(
            model_name='studentfee',
            name='student',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='StudentApp.student'),
        ),
    ]