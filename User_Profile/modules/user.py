import requests


def get_user_info(request):
    user_info = dict(first_name=request.user.first_name,
                     last_name=request.user.last_name)

    url = 'https://api.vk.com/method/friends.get?'
    social = request.user.social_auth.get(provider='vk-oauth2')

    params = {
        'fields': 'photo_100',
        'count': 5,
        'v': 5.51,
        'access_token': social.extra_data['access_token']
    }

    response = requests.get(url, params=params).json()

    if response['response']['count']:
        user_info['friends_list'] = response['response']['items']

    return user_info
