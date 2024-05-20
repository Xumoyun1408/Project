# Generated by Django 5.0.6 on 2024-05-18 10:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('air', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Air',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField()),
                ('image', models.ImageField(null=True, upload_to='air_images')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='airs', to='air.category')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
