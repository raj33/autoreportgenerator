# Generated by Django 2.0.7 on 2018-08-11 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adverse', '0013_question_closed_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='District',
        ),
        migrations.RemoveField(
            model_name='question',
            name='Status',
        ),
        migrations.RemoveField(
            model_name='question',
            name='closed_date',
        ),
        migrations.RemoveField(
            model_name='question',
            name='complaint_type',
        ),
        migrations.RemoveField(
            model_name='question',
            name='crn_no',
        ),
        migrations.RemoveField(
            model_name='question',
            name='page_no',
        ),
        migrations.RemoveField(
            model_name='question',
            name='paper',
        ),
        migrations.RemoveField(
            model_name='question',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='question',
            name='ulb',
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=200, verbose_name='CCC EMPLOYEE'),
        ),
    ]
