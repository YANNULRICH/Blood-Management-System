# Generated by Django 5.0.7 on 2024-09-10 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mblood', '0009_alter_bloodbank_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodbag',
            name='quantity',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='blooddonation',
            name='quantity',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='bloodtype',
            name='quantity',
            field=models.IntegerField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='command',
            name='quantity',
            field=models.IntegerField(max_length=100),
        ),
    ]
