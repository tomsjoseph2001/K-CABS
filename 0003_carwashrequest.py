# Generated by Django 4.2.7 on 2024-02-19 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_booking_total_km'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarWashRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(choices=[('interior', 'Interior'), ('exterior', 'Exterior'), ('both', 'Both Interior and Exterior')], max_length=20)),
                ('date_needed', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
