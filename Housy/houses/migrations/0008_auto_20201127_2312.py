# Generated by Django 3.1.3 on 2020-11-27 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0007_auto_20201127_2309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='featuredproperties',
            old_name='proprety_types',
            new_name='property_types',
        ),
    ]
