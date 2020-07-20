from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.shortcuts import render
from .user import get_user_info
import json


def login_response(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/profile')

    return render(request, 'login_page.html')


def logout_response(request):
    logout(request)
    response = HttpResponseRedirect('/login')
    response.delete_cookie("user_info")
    return response


def profile_response(request):
    if request.user.is_authenticated:
        if request.COOKIES.get('user_info'):
            user_info = json.loads(request.COOKIES.get('user_info'))
            return render(request, 'profile_page.html', user_info)

        user_info = get_user_info(request)
        response = render(request, 'profile_page.html', user_info)
        response.set_cookie('user_info', json.dumps(user_info))

        return response

    return HttpResponseRedirect('/login')
