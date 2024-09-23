# Generated by Django 5.0.7 on 2024-09-12 09:37

import blood.utils.random
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mblood', '0011_remove_bloodtype_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodbank',
            name='name',
            field=models.CharField(default='A', max_length=100),
        ),
        migrations.AlterField(
            model_name='bloodbag',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bloodbank',
            name='code',
            field=models.CharField(default=blood.utils.random.generate_unique_code, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='blooddonation',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='command',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]