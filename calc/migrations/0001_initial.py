# Generated by Django 2.2.7 on 2019-11-16 18:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bondinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
