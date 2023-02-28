# Generated by Django 4.1.7 on 2023-02-28 09:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0005_alter_evenement_even_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
        migrations.AlterField(
            model_name='evenement',
            name='even_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 28, 10, 37, 49, 299895), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='reserv_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 28, 10, 37, 49, 300895), verbose_name='Date de la réservation'),
        ),
    ]
