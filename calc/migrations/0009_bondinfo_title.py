# Generated by Django 2.2.7 on 2019-11-21 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0008_remove_bondinfo_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='bondinfo',
            name='Title',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
