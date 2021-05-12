import hashlib

from django.core.mail import send_mail
from django.template import loader

from App.models import Cart
from My_Shop.settings import EMAIL_HOST_USER, SERVER_HOST, SERVER_PORT


def hash_str(source):
    return hashlib.new('sha512', source.encode('utf-8')).hexdigest()


"""
將資料庫資料表字串加密成 512雜湊 編碼utf-8 預設2進制轉成16進制用在密碼上面
"""


def send_email_activate(username, receive, u_token):
    subject = '%s MyShop Activate' % username
    from_email = EMAIL_HOST_USER
    recipient_list = [receive, ]
    data = {
        'username': username,
        'activate_url': 'http://{}:{}/myshop/activate/?u_token={}'.format(SERVER_HOST, SERVER_PORT, u_token)
    }
    html_message = loader.get_template('user/activate.html').render(data)

    send_mail(subject=subject, message='', html_message=html_message, from_email=from_email,
              recipient_list=recipient_list)


def get_total_price():
    carts = Cart.objects.filter(c_is_select=True)
    total = 0
    for cart in carts:
        total += cart.c_goods_num * cart.c_goods.price
    return total
