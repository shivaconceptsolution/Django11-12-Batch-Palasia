# Generated by Django 2.0.6 on 2019-07-15 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rno', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('branch', models.CharField(max_length=200)),
                ('fees', models.IntegerField(max_length=200)),
            ],
        ),
    ]
