# Generated by Django 2.2.9 on 2021-04-15 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainNav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=225)),
                ('name', models.CharField(max_length=64)),
                ('trackid', models.IntegerField(default=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MainWheel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=225)),
                ('name', models.CharField(max_length=64)),
                ('trackid', models.IntegerField(default=1)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]