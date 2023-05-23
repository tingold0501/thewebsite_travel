# Generated by Django 4.2 on 2023-05-22 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('booking', '0002_rename_name_restaurant_title_remove_restaurant_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=20)),
                ('restaurant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='booking.restaurant')),
            ],
        ),
    ]
