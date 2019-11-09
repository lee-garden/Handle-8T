# Generated by Django 2.2.7 on 2019-11-09 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Province',
            fields=[
                ('province_code', models.IntegerField(primary_key=True, serialize=False)),
                ('province_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Borough',
            fields=[
                ('borough_code', models.IntegerField(primary_key=True, serialize=False)),
                ('borough_name', models.CharField(max_length=30)),
                ('province_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='city_api.Province')),
            ],
        ),
    ]
