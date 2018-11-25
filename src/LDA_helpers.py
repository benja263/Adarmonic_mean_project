import pandas as pd
import re
import nltk
from nltk.corpus import wordnet as wn
from collections import Counter

import gensim
from wordcloud import WordCloud
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel
from gensim.parsing.preprocessing import remove_stopwords

import matplotlib.pyplot as plt
import numpy as np


#---------------------------------------------------------


def get_lemma(word):
    '''Lemmatize the words into their roots'''
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma
    
#---------------------------------------------------------

def hashtagger(text):
    """Breaks up a hashtag into its composing words so they can be fed into LDA analysis
    Hashtags are split based on capitalized letters. Consecutive capitalized letters are not split
    Example: #MyDogIsCool returns #My Dog Is Cool. #NFA returns #NFA"""
    # Locate string of hashtag
    import re
    tags = re.findall(r'#\w+', text)
    tag_split = []
    for tag in tags:
        no_hash = tag[1:]
        tag_split.append(" ".join([a for a in re.split('([A-Z][a-z]+)', no_hash) if a])) # Separate out words    
    return ' '.join(tag_split) # return sentence


#---------------------------------------------------------

def hashtag_counter(text, do = 'extract'):
    """Function that allows extraction of hashtags with the option to count them
    do parameter can be to 'extract' the hashtags or to 'count' them"""
    import re
    from collections import Counter
    tags = re.findall(r'#\w+', text)
    tags = " ".join(tags)
    if do == 'count':
        hashtag_count = Counter(tags.split())
        return hashtag_count
    else: 
        return tags

    
#---------------------------------------------------------

def process_tweets(dataset, group_by = 'author', filter_language = 'English', extract_hashtags = True, filtersize = 3):
    """This function takes in the dataset in the format found directly from Kaggle. It filters by token length, 
    selectable language and has the option to extract hashtags into words. 
    
    The function returns the tokens as an array, with each 'sample' as a list of tokens written by a single 
    author. The function also returns the tags (hashtags) counts for each author
    
    The function takes in a parameter group_by that can be either 'hashtag' or 'author' (default). grouping by 
    hashtag retuns a dataset that has each row a concatenated number of tweets with that hashtag, while
    grouping by author concatenates all the tweets from the author"""
    import pandas as pd
    import re
    from nltk.corpus import wordnet as wn
    from collections import Counter

    pd.options.mode.chained_assignment = None  # default='warn', suppress the setting with copy warning

    # Filter for languages if true 
    if filter_language:
        # selecting content columns for subject categorization by language
        dataset = dataset[dataset.language == filter_language]
        cont = dataset.content
    else:
        cont = dataset.content
    
    content_filtered = cont.apply(lambda x: re.sub(r'http\S+', '', x)).apply(lambda x: re.sub(r"'|\"|`|:|\?|~|,|\.", '', x))\
                .apply(lambda x: remove_stopwords(x))


    # redefine content column for dataset
    dataset['content'] = content_filtered.values
    # Drop NaN values in content    
    dataset.dropna(axis=0,subset=['content'], inplace=True)
    # Get list of words that are stop words    
    en_stop = set(nltk.corpus.stopwords.words('english'))
    tokens = []
    
    ##### GROUP BY AUTHOR ######
    
    if group_by == 'author':
        tweets_concatenated = dataset.groupby('author')['content'].apply(lambda x : x.sum()
                                                                    if x.dtype=='float64' else ' '.join(x))
        content = tweets_concatenated.copy()
        if extract_hashtags == True:
            # Count the hashtag frequency for each user
            hashtag_count = tweets_concatenated.apply(lambda x: hashtag_counter(x, do='count'))
            # Extract words that are in hashtags
            hashtagged = tweets_concatenated.apply(lambda x: hashtagger(x))
            # Concatenate the words to the entire tweets
            hashtags_gone = hashtagged + tweets_concatenated
            # Remove hashtags since they are no longer needed and make all words lower case
            hashtags_gone = hashtags_gone.apply(lambda x: re.sub(r"#\w+", '', x)).apply(lambda x: x.lower())
            # Convert to NumPy array
            content = hashtags_gone.values
        content_tokens = [nltk.word_tokenize(x) for x in content]
        for sublist in content_tokens:
            tokens.append([get_lemma(token) for token in sublist if token not in en_stop and len(token) > 3])

        return tokens, hashtag_count
    
    ##### GROUP BY HASHTAG ######
    
    if group_by == 'hashtag':
        hashtag_column = dataset['content'].apply(lambda x: hashtag_counter(x))
        df_hashtags = pd.concat([dataset['content'], hashtag_column], axis=1)
        df_hashtags.columns = ['content', 'hashtags']
        
        
        # make the series that has as the index values the hashtag and the column that has the concatenated 
        # tweets.
        tweets_concatenated = df_hashtags.groupby('hashtags')['content'].apply(lambda x : x.sum()
                                                                    if x.dtype=='float64' else ' '.join(x))
        # remove the hashtag shit
        hashtags_gone = tweets_concatenated.apply(lambda x: re.sub(r"#\w+", '', x)).apply(lambda x: x.lower())
        content = hashtags_gone.values


        content_tokens = [nltk.word_tokenize(x) for x in content]
        for sublist in content_tokens:
            tokens.append([get_lemma(token) for token in sublist if token not in en_stop and len(token) > 3])
            
        return tweets_concatenated, tokens, hashtag_column