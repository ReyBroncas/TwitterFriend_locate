import urllib.request
import twhandle
import json
import os.path


def get_friend_data(api_reference, user_id, friend_id):
    if not os.path.isfile(f'cache/{user_id}/{friend_id}_data.json'):
        # print(f'Geting {friend_id} data from net...')
        url = twhandle.augment(api_reference, {'user_id': friend_id})
        data = urllib.request.urlopen(url).read()
        js = json.loads(data)
        with open(f'cache/{user_id}/{friend_id}_data.json', 'w') as outfile:
            json.dump(js, outfile)
        return js['name'], js['location'], js['profile_image_url']
    else:
        # print(f'Reading {friend_id} in cache...')
        with open(f'cache/{user_id}/{friend_id}_data.json', 'r') as file:
            decoded_friend = json.load(file)
        return decoded_friend['name'], decoded_friend['location'], decoded_friend['profile_image_url']


def get_user_friends(api_reference, username):
    if not os.path.isfile(f'cache/{username}/{username}_friends.json'):
        # print(f'Getting {username} data from net...')
        url = twhandle.augment(api_reference, {'screen_name': username, 'count': '3141592653'})
        data = urllib.request.urlopen(url).read()
        js = json.loads(data)
        os.makedirs(f'cache/{username}')
        with open(f'cache/{username}/{username}_friends.json', 'w') as outfile:
            json.dump(js, outfile)
        return js['ids']
    else:
        # print(f'Reading {username} cache...')
        with open(f'cache/{username}/{username}_friends.json', 'r') as file:
            decoded_user = json.load(file)
        return decoded_user['ids']


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
