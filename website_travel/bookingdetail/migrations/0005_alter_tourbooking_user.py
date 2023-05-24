# Generated by Django 4.2 on 2023-05-24 03:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rigister', '0002_user_delete_signup'),
        ('bookingdetail', '0004_tourbooking_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourbooking',
            name='user',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='rigister.user'),
            preserve_default=False,
        ),
    ]
