# Generated by Django 4.2 on 2023-05-24 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookingdetail', '0006_alter_tourbooking_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TourBooking',
        ),
    ]
