# Generated by Django 2.2.5 on 2020-03-19 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0002_auto_20200318_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='st_id',
            field=models.CharField(max_length=8, unique=True),
        ),
    ]