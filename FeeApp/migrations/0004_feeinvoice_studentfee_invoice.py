# Generated by Django 5.0.9 on 2024-11-11 14:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FeeApp', '0003_studentfee_class_id_studentfee_created_at_and_more'),
        ('StudentApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeeInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('gst_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateTimeField(auto_now=True)),
                ('student', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='StudentApp.student')),
            ],
        ),
        migrations.AddField(
            model_name='studentfee',
            name='invoice',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='FeeApp.feeinvoice'),
            preserve_default=False,
        ),
    ]
