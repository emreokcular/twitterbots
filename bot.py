from logging import error
import sys
import readchar # Only for local machine.
from helpers import *

"""
Press n for generating new random combination.
Press y for tweet. Then q for quit.
"""

twitter_auth_filename = sys.argv[1]
order = sys.argv[2] 
api = authenticate(twitter_auth_filename)

archive_set = load_archive()
pairs = load_words()

adjectives,nouns,adverbs,verbs = create_lists(pairs)

print("Bot is UP!")

while True:
    inp = "n"
    
    while inp=="n":
    
        word = get_random_words(adjectives,nouns,adverbs,verbs,order,archive_set)
        print("\n",word,"\n")
        inp = readchar.readchar()
    if inp =="y":
        api.update_status(word)
        print("\n Tweeted successfully! \n")
        inp = readchar.readchar()
    if inp == "q":
        break