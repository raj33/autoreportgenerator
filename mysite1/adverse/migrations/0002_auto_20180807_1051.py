# Generated by Django 2.0.7 on 2018-08-07 05:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adverse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='District',
            field=models.CharField(default=django.utils.timezone.now, max_length=200, verbose_name='District'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Greivance Date'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=200, verbose_name='CCC EMPLOYEE'),
        ),
    ]