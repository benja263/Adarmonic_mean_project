import os
from nltk.corpus import stopwords
import string
from nltk.stem import SnowballStemmer
from nltk.stem.porter import *

dir = os.path.dirname(__file__)
DOWNLOADED_DICTIONARY_PATH = os.path.join(dir,'Test_Set_3802_Pairs.txt')

downloaded_dictionary = {}
f = open(DOWNLOADED_DICTIONARY_PATH, 'rb')
for word in f:
    word = word.decode('utf8')
    word = word.split()
    downloaded_dictionary[word[1]] = word[3]
f.close()


def clean(tweet):
    """
    Function that cleans the tweet using the functions above and some regular expressions
    to reduce the noise

    Arguments: tweet (the tweet)

    """
    #Separates the contractions and the punctuation
    stop_words = set(stopwords.words('english'))
    words = tweet.split(" ")
    punctuations = string.punctuation
    punctuations = punctuations.replace("-", "")
    punctuations = punctuations.replace("'", "")
    table = str.maketrans('', '', punctuations)
    cleaned_tweet = ""
    stemmer = SnowballStemmer('english')
    for word in words:
        if "http" not in word and word not in stop_words and not word.startswith('#') and not word.startswith('@'):
            lower_word = word.lower()
            lower_word = lower_word.translate(table)
            if lower_word.isalpha():
                cleaned_tweet += stemmer.stem(lower_word) + " "
    return correct_spell(cleaned_tweet)


def correct_spell(tweet):
    """
    Function that uses the three dictionaries that we described above and replace noisy words

    Arguments: tweet (the tweet)

    """

    tweet = tweet.split()
    for i in range(len(tweet)):
        if tweet[i] in downloaded_dictionary.keys():
            tweet[i] = downloaded_dictionary[tweet[i]]
    tweet = ' '.join(tweet)
    return tweet
