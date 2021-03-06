# Generated by Django 2.2.7 on 2019-11-16 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0002_auto_20191116_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='bondinfo',
            name='Minimum_monthly_income_required',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bondinfo',
            name='Monthly_payment',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bondinfo',
            name='Total_interest',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bondinfo',
            name='Total_onceoff_payment',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bondinfo',
            name='House_price',
            field=models.FloatField(),
        ),
    ]
