# Generated by Django 4.2 on 2023-05-23 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formsdashboard', '0014_restaurant'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('restaurant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='formsdashboard.restaurant')),
            ],
        ),
    ]