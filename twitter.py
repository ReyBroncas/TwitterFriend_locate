import urllib.request
import twurl
import json

TWITTER_URL = 'https://api.twitter.com/1.1/friends/ids.json'

while True:
    acct = input('Enter Twitter Account: ')
    if len(acct) < 1: break
    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '100'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url)
    data = connection.read()
    js = json.loads(data)
    print(json.dumps(js, indent=4))
