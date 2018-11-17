import os
from nltk.corpus import stopwords
import string
from nltk.stem import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
import nltk

nltk.download('wordnet')
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
s
    """
    #Separates the contractions and the punctuation

    stop_words = set(stopwords.words('english'))
    stop_words.update(set(['and', 'i', 'a', 'and', 'so', 'arnt', 'this', 'when', 'it', 'many', 'Many', 'so', 'cant',
                            'Yes', 'yes', 'No', 'no', 'these', 'these', "can't", "won't", 'get', 'you', 'like', 'him',
                       'her', 'his', 'hers', 'amp', 'via', 'this', 'say', 'just', 'the', 'see', 'sit', 'use', 'one',
                           'want', 'make', 'look', 'know', 'thing' , 'need', 'would']))
    words = tweet.split(" ")
    punctuations = string.punctuation
    punctuations = punctuations.replace("-", "")
    punctuations = punctuations.replace("'", "")
    table = str.maketrans('', '', punctuations)
    cleaned_tweet = ""
    lemmatizer = WordNetLemmatizer()
    for word in words:
        lower_word = word.lower()
        lower_word = lower_word.translate(table)
        lower_word = lemmatizer.lemmatize(lower_word)
        if "http" not in lower_word and lower_word not in stop_words and not lower_word.startswith('#') and not lower_word.startswith('@')\
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
