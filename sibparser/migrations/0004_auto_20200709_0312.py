# Generated by Django 2.2.12 on 2020-07-09 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sibparser', '0003_auto_20200708_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parsedsite',
            name='encoding',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
