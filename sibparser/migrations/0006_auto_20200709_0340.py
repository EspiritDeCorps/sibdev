# Generated by Django 2.2.12 on 2020-07-09 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sibparser', '0005_auto_20200709_0332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parsedsite',
            name='encoding',
            field=models.CharField(default=' ', max_length=20),
        ),
        migrations.AlterField(
            model_name='parsedsite',
            name='successfully',
            field=models.BooleanField(default=' '),
        ),
        migrations.AlterField(
            model_name='parsedsite',
            name='title',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]
