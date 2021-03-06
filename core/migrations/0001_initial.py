# Generated by Django 4.0.4 on 2022-05-01 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=30)),
                ('language', models.CharField(max_length=2)),
                ('currency', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.FloatField()),
                ('geojson', models.JSONField()),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.provider')),
            ],
        ),
    ]
