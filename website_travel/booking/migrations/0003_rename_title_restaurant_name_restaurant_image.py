# Generated by Django 4.2 on 2023-05-23 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_rename_name_restaurant_title_remove_restaurant_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
