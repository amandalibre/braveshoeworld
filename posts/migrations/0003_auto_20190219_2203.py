# Generated by Django 2.1.7 on 2019-02-20 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20190219_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='brand',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='color',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='post',
            name='link',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
