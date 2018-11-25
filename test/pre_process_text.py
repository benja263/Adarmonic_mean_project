import os
from nltk.corpus import stopwords
import string
from nltk.stem import WordNetLemmatizer
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
    # stop_words.update(set(['via','look', 'call', 'say', 'like', 'want', 'get', 'one', 'amp', 'trump']))
    words = tweet.split(" ")
    punctuations = string.punctuation
    punctuations = punctuations.replace("-", "")
    punctuations = punctuations.replace("'", "")
    table = str.maketrans('', '', punctuations)
    wordnet_lemmatizer = WordNetLemmatizer()
    cleaned_tweet = ""
    for word in words:
        word = word.translate(table)
        lower_word = word.lower()
        lower_word = wordnet_lemmatizer.lemmatize(lower_word)
        if "http" not in lower_word and lower_word not in stop_words and not lower_word.startswith('#') and not lower_word.startswith('@') \
                and lower_word.isalpha() and len(lower_word) > 2:
            cleaned_tweet += lower_word + " "
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
