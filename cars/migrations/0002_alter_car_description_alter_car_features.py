# Generated by Django 4.1.6 on 2023-02-08 09:16

import ckeditor.fields
from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='features',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Cruise Control', 'Cruise Control'), ('Navigation System', 'Navigation System'), ('Airbags', 'Airbags'), ('Air Conditioning', 'Air Conditioning'), ('Heated Seating', 'Heated Seating'), ('Alarm System', 'Alarm System'), ('ParkAssist', 'ParkAssist'), ('Power Steering', 'Power Steering'), ('Backup Camera', 'Backup Camera'), ('Traction Control', 'Traction Control'), ('All Wheel Drive', 'All Wheel Drive'), ('Auto Dimming Mirrors', 'Auto Dimming Mirrors'), ('Music System', 'Music System'), ('Sun Roof', 'Sun Roof'), ('Moon Roof', 'Moon Roof')], max_length=100),
        ),
    ]
