# Generated by Django 2.1.7 on 2019-02-20 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shoe', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=10)),
                ('store', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
