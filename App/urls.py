"""My_Shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from App import views

app_name = 'myshop'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('market/', views.market, name='market'),
    path('marketwithparams/<type_id>/<child_cid>/<order_rule>/', views.market_with_params, name='market_with_params'),
    path('cart/', views.cart, name='cart'),
    path('mine/', views.mine, name='mine'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('checkuser/', views.check_user, name='check_user'),
    path('checkemail/', views.check_email, name='check_email'),
    path('logout/', views.logout, name='logout'),
    path('activate/', views.activate, name='activate'),
    path('addtocart/', views.add_to_cart, name='add_to_cart'),
    path('changecartstate/', views.change_cart_state, name='change_cart_state'),
    path('subshopping/', views.sub_shopping, name='sub_shopping'),
    path('allselect/', views.all_select, name='all_select'),
    path('makeorder/', views.make_order, name='make_order'),
    path('orderdetail/', views.order_detail, name='order_detail'),
    path('orderlistnotpay/', views.order_list_not_pay, name='order_list_not_pay'),
    path('payed/', views.payed, name='payed'),

]

"""
舊版參數寫法'marketwithparams/(?P<typeid>\d+)/'
"""
