# Generated by Django 5.0.6 on 2024-05-19 14:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('air', '0006_remove_reys_air_reys_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reys',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reyses', to='air.category'),
        ),
    ]
