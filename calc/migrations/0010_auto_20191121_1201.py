# Generated by Django 2.2.7 on 2019-11-21 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0009_bondinfo_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bondinfo',
            name='Title',
            field=models.CharField(max_length=200),
        ),
    ]
