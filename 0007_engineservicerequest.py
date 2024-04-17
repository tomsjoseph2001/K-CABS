# Generated by Django 4.2.7 on 2024-02-19 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_tyreupgraderequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='EngineServiceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(choices=[('oil-change', 'Oil Change'), ('engine-tuning', 'Engine Tuning'), ('diagnostics', 'Diagnostics')], max_length=20)),
                ('date_needed', models.DateField()),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.driver')),
            ],
        ),
    ]
