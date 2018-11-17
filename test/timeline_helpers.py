# Functions for data exploration and plotting

# imports

import pandas as pd
import plotly.graph_objs as go

#----------------------------------------------
def count_language(lang, language_time):
    """The function takes in a language as a DEFINE_string
    and goes through a dataframe that has one column named
    language and another one that has publish_date. It then
    groups the tweets by month and returns the sum of the
    tweets during the time period"""

    filt = language_time[language_time.language == lang].copy()
    filt['language_num'] = filt.language.map({lang:1})
    return filt.groupby(pd.Grouper(key='publish_date', freq='1M')).sum()


#----------------------------------------------

def trace_generator_language(lang_df):
    """This function generates the data that will be used
    as input for the iplot function. It prepares the labels
    from the index"""
    data = []
    for lang in lang_df.language.value_counts().index.values[0:10]:
        filtered=count_language(lang, lang_df)
        strd = pd.Series(filtered.index.strftime('%Y-%m-%d %H-%M-%S'))
        xlabels = list(strd.apply(lambda x: x[0:7]))
        trace = go.Scatter(x=xlabels,
                            y=filtered.language_num.values,
                            fill='tozeroy',
                            mode= 'none',
                            name=lang)
        data.append(trace)

    return data

#----------------------------------------------

def count_accounttype(account, accounttype_time):
    """Same thing as count_language. See above, except takes if __name__ == '__main__':
    an account category string"""
    filt = accounttype_time[accounttype_time.account_category == account].copy()
    filt['account_num'] = filt.account_category.map({account:1})
    return filt.groupby(pd.Grouper(key='publish_date', freq='1M')).sum()

#----------------------------------------------

def trace_generator_account(account_df):
    """Same thing as trace_generator_language except for account
    category variable"""
    data = []
    for account in account_df.account_category.value_counts().index.values[0:10]:
        filtered=count_accounttype(account, account_df)
        strd = pd.Series(filtered.index.strftime('%Y-%m-%d %H-%M-%S'))
        xlabels = list(strd.apply(lambda x: x[0:7]))
        trace = dict(x=xlabels,
                     y=filtered.account_num.values,
                     mode= 'lines',
                     stackgroup='one',
                     groupnorm='percent',
                     name=account)
        data.append(trace)

    return data

#----------------------------------------------

def count_followers(category, bubble_data):
    """Used to create the bubble graphs, returns a DataFrame
    with the follower numbers as well as the number of tweets
    in the time intervals"""
    filt = bubble_data[bubble_data.account_category == category].copy()
    # filt.drop(['account_category'], axis=1, inplace=True)
    filt['tweet_category_num'] = filt.account_category.map({category:1})
    return filt.groupby(pd.Grouper(key='publish_date', freq='3M')).sum()


#----------------------------------------------

def do_layout(xlabel, ylabel, title):
    """Prepare layout for axis labeling plotly"""
    layout = go.Layout(
        title=title,
        xaxis=dict(
            title=xlabel,
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f')),
        yaxis=dict(
            title=ylabel,
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f')))

    return layout
