# Generated by Django 3.2.20 on 2023-11-06 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountno', models.CharField(max_length=100)),
                ('ifsccode', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('amount', models.FloatField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicleregno', models.CharField(max_length=20)),
                ('vehiclemodel', models.CharField(max_length=10)),
                ('enginenumber', models.CharField(max_length=10)),
                ('totalseats', models.IntegerField()),
                ('ac_nonac', models.CharField(max_length=10)),
                ('vehicletype', models.CharField(max_length=25)),
                ('photo', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('photo', models.CharField(default='A', max_length=500)),
                ('housename', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.login')),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('housename', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('photo', models.CharField(max_length=100)),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.login')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('status', models.CharField(default='pending', max_length=20)),
                ('reply', models.CharField(default='pending', max_length=20)),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]
