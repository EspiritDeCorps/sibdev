# Generated by Django 2.2.12 on 2020-07-09 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sibparser', '0006_auto_20200709_0340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parsedsite',
            name='successfully',
            field=models.BooleanField(default=True),
        ),
    ]
