# Twitter bot ideas and implementations

API + creativity + Twitter = awesomeness!

In this repo you can find list of Twitter bot ideas and its implementations with [Tweepy](https://www.tweepy.org/).

## Twitter Bots:

1. [Random Words Twitter Bot](https://twitter.com/kelimebot) - *Created in January*

Randomly combines word pairs from dictionary.

2. Average Score Calculator Bot - *Loading*

Calulates average score from the replies of mentioned tweet.

3. Trending words bot - *Loading*

Application of topic modelling for tweets. Most tweeted words are categorized with NMF and LDA methods daily.

4. Viral Bot - *Loading*

Curated lis of top tweeted url links other than top lists in spotify and youtube trending.

## Set up notes

### How to install Tweepy

First, check your Python version with ``python3 --version`` or ``python --version`` on console (terminal/shell/command prompt).

#### If you don't have Python 3 installed (if the above command fails):

Install Python 3 on your computer (https://www.python.org/downloads/).

#### If you have Python 3.6, you can just run:

``pip3 install tweepy``

#### If you have Python 3.7, run the following instead:

``pip3 install -U git+https://github.com/tweepy/tweepy.git@2efe385fc69385b57733f747ee62e6be12a1338b``

If the above command doesn't work, try replacing ``pip3`` with ``pip`` also.

#### If you have Python 3.7 and want to use pipenv, use:

``pipenv install -e git+https://github.com/tweepy/tweepy.git@2efe385fc69385b57733f747ee62e6be12a1338b#egg=tweepy``

---

## Files
- **twitter_bot.py** - This is the main file that includes all the logic.
- **archive.txt** - This file contains all the generated word collections and also tweets.
- **clean_words.txt** - List of all words in dictionary paired with types such as noun,verb, adverb etc.