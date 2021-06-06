import tweepy
from typing import List
import random


ARCHIVE_FILE = "archive.txt"
WORDS_FILE = "clean_words.txt"

noun_conjunctions = ["ve","veya","ile","ya da","gibi"] # "bir başka deyişle"
verb_conjunctions = ["ve","veya","ya da","hatta","belki de"] # "bir başka deyişle"
dual_conjunctions = ["ile","yoksa","gibi"]

def loadkeys(filename:str) ->List:
    """"
    load twitter api keys/tokens from CSV file with form
    consumer_key, consumer_secret, access_token, access_token_secret
    """
    with open(filename) as f:
        items = f.readline().strip().split(', ')
        return items

def authenticate(twitter_auth_filename:str):
    """
    Given a file name containing the Twitter keys and tokens,
    create and return a tweepy API object.
    """
    keys = loadkeys(twitter_auth_filename)
    consumer_key = keys[0]
    consumer_secret = keys[1]
    access_token = keys[2]
    access_token_secret = keys[3]

    # authorization of consumer key and consumer secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True)
    return api

def load_words():
    """
    Loads words dataset from .txt file. Returns word:type pairs in a dictionary.
    """
    pairs = dict()
    f = open(WORDS_FILE, 'r')
    contents = f.read()
    lines = contents.split("\n")
    for line in lines:
        parts = line.split(",")
        pairs[parts[0]] = parts[1]
    f.close()
    return pairs

def load_archive():
    with open(ARCHIVE_FILE,"r") as f:
        contents = f.read()
        lines = contents.split("\n")
    return set(map(str.strip, lines))        

def write_to_archive(word:str):
    with open(ARCHIVE_FILE,"a") as f:
        f.write(word)
        f.write("\n")

def create_lists(final):
    verbs = []
    nouns = []
    adjectives = []
    adverbs = []
    for item in final:
        if final[item]=="fiil":
            verbs.append(item)
        if final[item]=="isim":
            nouns.append(item)
        if final[item]=="sıfat":
            adjectives.append(item)
        if final[item]=="zarf":
            adverbs.append(item)
    return adjectives,nouns,adverbs,verbs


def get_random_words(adjectives,nouns,adverbs,verbs,option,archive_set):
    word = ""
    if option =="ii": # adjective + noun + noun_conjunction + adjective + noun
        while word in archive_set:
            word = " ".join([random.choice(adjectives),random.choice(nouns),random.choice(noun_conjunctions),random.choice(adjectives),random.choice(nouns)])
    elif option =="ff": # adverb + verb + verb_conjunction + adverb + verb
        while word in archive_set:
            word = " ".join([random.choice(adverbs),random.choice(verbs),random.choice(verb_conjunctions),random.choice(adverbs),random.choice(verbs)])
    elif option =="if": # adjective + noun + dual_conjunction + adverb + verb
        while word in archive_set:
            word = " ".join([random.choice(adjectives),random.choice(nouns),random.choice(dual_conjunctions),random.choice(adverbs),random.choice(verbs)])
    elif option =="iii": # adjective + adjective + noun
        while word in archive_set:
            word = " ".join([random.choice(adjectives),random.choice(adjectives),random.choice(nouns)])
    elif option =="fff": # adverb + adverb + verb
        while word in archive_set:
            word = " ".join([random.choice(adverbs),random.choice(adverbs),random.choice(verbs)])
    else:
        raise ValueError("Failed to tweet! Check the order input.")
    
    write_to_archive(word) # Write to archive.txt 
    
    return word    