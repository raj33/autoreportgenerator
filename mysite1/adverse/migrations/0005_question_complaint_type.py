# Generated by Django 2.0.7 on 2018-08-07 07:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adverse', '0004_question_crn_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='complaint_type',
            field=models.CharField(default=django.utils.timezone.now, max_length=200, verbose_name='Complaint Type'),
            preserve_default=False,
        ),
    ]
