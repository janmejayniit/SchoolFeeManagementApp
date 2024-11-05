# Generated by Django 5.0.9 on 2024-11-05 06:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FeeApp', '0001_initial'),
        ('StudentApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentFee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('fee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FeeApp.feemaster')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentApp.student')),
            ],
        ),
    ]
