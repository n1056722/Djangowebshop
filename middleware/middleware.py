
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from App.models import User

REQUIRE_LOGIN_JSON = [
    '/myshop/addtocart/',
    '/myshop/changecartstate/',
    '/myshop/makeorder/',
]
REQUIRE_LOGIN = [
    '/myshop/cart/',
    '/myshop/orderdetail/',
    '/myshop/orderlistnotpay/',
]


class LoginMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path in REQUIRE_LOGIN_JSON:
            user_id = request.session.get('user_id')
            if user_id:
                try:
                    user = User.objects.get(pk=user_id)
                    request.user = user
                except:
                    data = {
                        'status': 302,
                        'msg': 'user not available',
                    }
                    return JsonResponse(data=data)
            else:
                data = {
                    'status': 302,
                    'msg': 'user not login',
                }
                return JsonResponse(data=data)
        if request.path in REQUIRE_LOGIN:
            user_id = request.session.get('user_id')
            if user_id:
                try:
                    user = User.objects.get(pk=user_id)
                    request.user = user
                except:
                    return redirect(reverse('myshop:login'))
            else:
                return redirect(reverse('myshop:login'))
