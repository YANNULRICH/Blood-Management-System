# Generated by Django 5.0.7 on 2024-09-09 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mblood', '0007_remove_bloodbank_quantity_a_minus_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bloodbank',
            options={'verbose_name': 'Blood Bank', 'verbose_name_plural': 'Blood Banks'},
        ),
    ]
