# Generated by Django 2.2.9 on 2021-04-16 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainMustBuy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=225, verbose_name='img')),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                ('trackid', models.IntegerField(default=1, verbose_name='trackid')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='mainnav',
            name='img',
            field=models.CharField(max_length=225, verbose_name='img'),
        ),
        migrations.AlterField(
            model_name='mainnav',
            name='name',
            field=models.CharField(max_length=64, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='mainnav',
            name='trackid',
            field=models.IntegerField(default=1, verbose_name='trackid'),
        ),
        migrations.AlterField(
            model_name='mainwheel',
            name='img',
            field=models.CharField(max_length=225, verbose_name='img'),
        ),
        migrations.AlterField(
            model_name='mainwheel',
            name='name',
            field=models.CharField(max_length=64, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='mainwheel',
            name='trackid',
            field=models.IntegerField(default=1, verbose_name='trackid'),
        ),
    ]
