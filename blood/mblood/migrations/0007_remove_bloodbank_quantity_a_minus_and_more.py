# Generated by Django 5.0.7 on 2024-09-06 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mblood', '0006_remove_bloodbank_quantity_bloodbank_quantity_a_minus_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloodbank',
            name='quantity_a_minus',
        ),
        migrations.RemoveField(
            model_name='bloodbank',
            name='quantity_a_plus',
        ),
        migrations.RemoveField(
            model_name='bloodbank',
            name='quantity_ab_minus',
        ),
        migrations.RemoveField(
            model_name='bloodbank',
            name='quantity_ab_plus',
        ),
        migrations.RemoveField(
            model_name='bloodbank',
            name='quantity_b_minus',
        ),
        migrations.RemoveField(
            model_name='bloodbank',
            name='quantity_b_plus',
        ),
        migrations.RemoveField(
            model_name='bloodbank',
            name='quantity_o_minus',
        ),
        migrations.RemoveField(
            model_name='bloodbank',
            name='quantity_o_plus',
        ),
    ]