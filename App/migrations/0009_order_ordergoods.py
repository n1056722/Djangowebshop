# Generated by Django 2.2.9 on 2021-05-07 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_price', models.PositiveIntegerField(default=0)),
                ('o_time', models.DateTimeField(auto_now=True)),
                ('o_status', models.PositiveIntegerField(default=1)),
                ('o_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.User')),
            ],
        ),
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_goods_num', models.PositiveIntegerField(default=1)),
                ('o_goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Goods')),
                ('o_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Order')),
            ],
        ),
    ]
