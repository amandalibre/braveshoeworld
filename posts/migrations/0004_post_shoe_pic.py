# Generated by Django 2.1.7 on 2019-02-20 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20190219_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='shoe_pic',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
