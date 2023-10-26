# Generated by Django 4.2.6 on 2023-10-26 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
        ('lostperson', '0004_remove_lostperson_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='lostperson',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='locations.location'),
        ),
    ]