import essential
import urllib.error
import pprint
import time
TWITTER_USER_FOLLOWERS = 'https://api.twitter.com/1.1/friends/ids.json'
TWITTER_USER_DATA = 'https://api.twitter.com/1.1/users/show.json'


while True:
    ACCT = input('Enter Twitter Account username: ')
    if len(ACCT) < 1:
        break
    try:
        friends_data = essential.get_user_friends(TWITTER_USER_FOLLOWERS, ACCT)
    except urllib.error.HTTPError:
        print('There is no user with this username')
        continue

    FRIENDS_NUMBER = int(input('Enter number of friends to display: '))
    if int(FRIENDS_NUMBER) > len(friends_data):
        FRIENDS_NUMBER = len(friends_data)

    friends_dict = {}
    for i in range(FRIENDS_NUMBER):
        data = essential.get_friend_data(TWITTER_USER_DATA, ACCT, friends_data[i])
        friends_dict.setdefault(data[0],{})
        friends_dict[data[0]].setdefault('location',data[1])
        friends_dict[data[0]].setdefault('image', data[-1])
        time.sleep(1.5)
    pprint.pprint(friends_dict)
