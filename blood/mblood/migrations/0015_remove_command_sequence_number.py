# Generated by Django 5.0.7 on 2024-09-19 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mblood', '0014_command_sequence_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='command',
            name='sequence_number',
        ),
    ]
