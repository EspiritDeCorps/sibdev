# Generated by Django 2.2.12 on 2020-07-09 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sibparser', '0007_auto_20200709_0350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='site',
            name='timeshift',
        ),
        migrations.AddField(
            model_name='site',
            name='timeshiftMinutes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='site',
            name='timeshiftSeconds',
            field=models.IntegerField(default=0),
        ),
    ]