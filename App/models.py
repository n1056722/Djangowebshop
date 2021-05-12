from django.db import models

# Create your models here.
from django.db.models import CASCADE

from App.views_constant import ORDER_STATUS_NOT_PAY


class Main(models.Model):
    """
    主頁面的模型
    """
    img = models.CharField(
        'img',
        max_length=225,
    )
    name = models.CharField(
        'name',
        max_length=64,
    )
    track_id = models.IntegerField(
        'track_id',
        default=1,
    )

    class Meta:
        abstract = True


class MainWheel(Main):
    """
    App_wheel(img.name.track_id)
    繼承主頁面的模型
    """


class MainNav(Main):
    """
    App_nav(img.name.track_id)
    繼承主頁面的模型
    """


class MainMustBuy(Main):
    """
    App_must_buy(img.name.track_id)
    繼承主頁面的模型
    """


class FoodType(models.Model):
    """
    App_food_type(type_id.type_name.child_type_names.type_sort)
    """
    type_id = models.IntegerField(
        'type_id',
        default=1,
        null=True,
    )
    type_name = models.CharField(
        'type_name',
        max_length=32,
        null=True,
    )
    child_type_names = models.CharField(
        'child_type_names',
        max_length=255,
        null=True,

    )
    type_sort = models.IntegerField(
        'type_sort',
        default=1,
        null=True,
    )


class Goods(models.Model):
    """
    App_goods(product_id,product_img,product_name,product_longname,is_my_shop,pmd_esc,specifics,price,market_price,category_id,child_cid,child_cid_name,dealer_id,store_nums,product_num)
    """
    product_id = models.IntegerField(
        'product_id',
        default=1,
    )
    product_img = models.CharField(
        'product_img',
        max_length=255,
    )
    product_name = models.CharField(
        'product_name',
        max_length=128,
    )
    product_longname = models.CharField(
        'product_longname',
        max_length=255,
    )
    is_my_shop = models.BooleanField(
        'is_my_shop',
        default=False,
    )
    pmd_esc = models.BooleanField(
        'pmd_esc',
        default=False,
    )
    specifics = models.CharField(
        'specifics',
        max_length=64,
    )
    price = models.IntegerField(
        'price',
        default=0,
    )
    market_price = models.IntegerField(
        'market_price',
        default=1,
    )
    category_id = models.IntegerField(
        'category_id',
        default=1,
    )
    child_cid = models.IntegerField(
        'child_cid',
        default=1,
    )
    child_cid_name = models.CharField(
        'child_cid_name',
        max_length=128,
    )
    dealer_id = models.IntegerField(
        'dealer_id',
        default=1,
    )
    store_nums = models.IntegerField(
        'store_nums',
        default=1,
    )
    product_num = models.IntegerField(
        'product_num',
        default=1,
    )


class User(models.Model):
    u_username = models.CharField(
        max_length=32,
        unique=True,
    )
    u_password = models.CharField(
        max_length=256,
    )
    u_email = models.CharField(
        max_length=64,
        unique=True,
    )
    u_icon = models.ImageField(
        upload_to='icons/%Y/%m/%d/',
    )
    is_active = models.BooleanField(
        default=False,
    )
    is_delete = models.BooleanField(
        default=False,
    )


class Cart(models.Model):
    c_user = models.ForeignKey(
        User,
        on_delete=CASCADE,
    )
    c_goods = models.ForeignKey(
        Goods,
        on_delete=CASCADE,
    )
    c_goods_num = models.IntegerField(
        default=1,
    )
    c_is_select = models.BooleanField(
        default=True,
    )


class Order(models.Model):
    o_user = models.ForeignKey(
        User,
        on_delete=CASCADE,
    )
    o_price = models.PositiveIntegerField(
        default=0,
    )
    o_time = models.DateTimeField(
        auto_now=True,
    )
    o_status = models.PositiveIntegerField(
        default=ORDER_STATUS_NOT_PAY,
    )


class OrderGoods(models.Model):
    o_order = models.ForeignKey(
        Order,
        on_delete=CASCADE,
    )
    o_goods = models.ForeignKey(
        Goods,
        on_delete=CASCADE,
    )
    o_goods_num = models.PositiveIntegerField(
        default=1,
    )
