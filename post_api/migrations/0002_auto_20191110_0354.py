# Generated by Django 2.2.7 on 2019-11-09 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='borough_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='city_api.Borough'),
        ),
    ]
