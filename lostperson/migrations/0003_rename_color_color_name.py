# Generated by Django 4.2.6 on 2023-10-26 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lostperson', '0002_bodytype_color_height_lostperson_age_skincomplexion_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='color',
            old_name='color',
            new_name='name',
        ),
    ]
