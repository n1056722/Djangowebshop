# Generated by Django 2.2.9 on 2021-04-19 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_auto_20210419_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(default=1, verbose_name='product_id')),
                ('product_img', models.CharField(max_length=255, verbose_name='product_img')),
                ('product_name', models.CharField(max_length=128, verbose_name='product_name')),
                ('product_longname', models.CharField(max_length=255, verbose_name='product_longname')),
                ('is_my_shop', models.BooleanField(default=False, verbose_name='is_my_shop')),
                ('pmd_esc', models.BooleanField(default=False, verbose_name='pmd_esc')),
                ('specifics', models.CharField(max_length=64, verbose_name='specifics')),
                ('price', models.IntegerField(default=0, verbose_name='price')),
                ('market_price', models.IntegerField(default=1, verbose_name='market_price')),
                ('category_id', models.IntegerField(default=1, verbose_name='category_id')),
                ('child_cid', models.IntegerField(default=1, verbose_name='child_cid')),
                ('child_cid_name', models.CharField(max_length=128, verbose_name='child_cid_name')),
                ('dealer_id', models.IntegerField(default=1, verbose_name='dealer_id')),
                ('store_nums', models.IntegerField(default=1, verbose_name='store_nums')),
                ('product_num', models.IntegerField(default=1, verbose_name='product_num')),
            ],
        ),
    ]
