# Generated by Django 5.0.9 on 2024-11-11 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FeeApp', '0004_feeinvoice_studentfee_invoice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentfee',
            name='student',
        ),
    ]
