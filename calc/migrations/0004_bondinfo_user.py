# Generated by Django 2.2.7 on 2019-11-20 02:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calc', '0003_auto_20191116_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='bondinfo',
            name='User',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
