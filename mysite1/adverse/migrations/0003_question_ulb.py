# Generated by Django 2.0.7 on 2018-08-07 07:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adverse', '0002_auto_20180807_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='ulb',
            field=models.CharField(default=django.utils.timezone.now, max_length=200, verbose_name='ULB'),
            preserve_default=False,
        ),
    ]
