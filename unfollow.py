import sys
import tweepy
import time
from helpers import *
"""
The python script for unfollowing non followers.
"""
twitter_auth_filename = sys.argv[1] 
api = authenticate(twitter_auth_filename)

SCREEN_NAME = "kelimebot"

followers = api.followers_ids(SCREEN_NAME)
friends = api.friends_ids(SCREEN_NAME)
counter = 0

for f in friends:

    print("Unfollowing {0}".format(api.get_user(f).screen_name))
    api.destroy_friendship(f)
    time.sleep(1)
    counter += 1


print(str(counter)+" accounts unfollowed.")