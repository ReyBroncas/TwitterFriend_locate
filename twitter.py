from geopy.geocoders import Nominatim
import twhandle
import urllib.request
import urllib.error
import json
TWITTER_USER_FOLLOWERS = 'https://api.twitter.com/1.1/friends/ids.json'
TWITTER_USER_DATA = 'https://api.twitter.com/1.1/users/show.json'


def get_twitter_json(api_reference, json_req):
    url = twhandle.augment(api_reference, json_req)
    data = urllib.request.urlopen(url).read()
    return json.loads(data)


def get_users_data(username, user_num):
    if len(username) < 1:
        return False
    users_data = {}
    try:
        friends_data = get_twitter_json(TWITTER_USER_FOLLOWERS,
                                        {'screen_name': username,
                                         'count': '3141592653'})['ids']
        user_num = int(user_num)
    except urllib.error.HTTPError or ValueError:
        return users_data
    if int(user_num) > len(friends_data):
        user_num = len(friends_data)
    geolocation = Nominatim(user_agent="map")
    for i in range(user_num):
        data = get_twitter_json(TWITTER_USER_DATA, {'user_id': friends_data[i]})
        geo_value = geolocation.geocode(data['location'], timeout=10)
        if geo_value is None: continue
        users_data.setdefault(data['name'], {})
        users_data[data['name']].setdefault(
            'location', (geo_value.latitude, geo_value.longitude))
        users_data[data['name']].setdefault('image', data['profile_image_url'])
    return users_data  # dict with coordinates
