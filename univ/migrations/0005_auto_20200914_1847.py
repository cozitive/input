# Generated by Django 3.0.8 on 2020-09-14 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('univ', '0004_auto_20200808_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='major',
            name='name',
            field=models.CharField(max_length=255, verbose_name='학과명'),
        ),
    ]