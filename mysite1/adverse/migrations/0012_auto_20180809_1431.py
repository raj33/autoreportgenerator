# Generated by Django 2.1 on 2018-08-09 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adverse', '0011_auto_20180809_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='page_no',
            field=models.CharField(max_length=200, verbose_name='Page no'),
        ),
        migrations.AlterField(
            model_name='question',
            name='paper',
            field=models.CharField(choices=[('EENADU', 'EENADU'), ('SAKSHI', 'SAKSHI')], max_length=200, verbose_name='Paper'),
        ),
    ]
