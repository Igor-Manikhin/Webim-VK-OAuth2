from .modules.responses import *


def index(request):
    return login_response(request)


def profile_view(request):
    return profile_response(request)


def logout_view(request):
    return logout_response(request)
