# Generated by Django 4.2 on 2023-05-23 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formsdashboard', '0017_alter_restaurantdetail_restaurant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantdetail',
            name='restaurant',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='formsdashboard.restaurant'),
        ),
    ]
