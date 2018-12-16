# Are Russian Trolls Good at their Jobs? The 2016 U.S. Elections: A Timeline Analysis

# Instructions to run the notebook (milestone 3)

The notebook is located in: `src\milestone_3`
If you don't want to run the whole code but still be able to see the interactive plots, you just need to run the dedicated cells we provided along the notebook as the graphs are all stored online. You will need to have the library Plotly installed:

``` $ pip install plotly ```

[Data-story](https://adarmonicteam.github.io/) Here you can see the data story of our project

# Abstract
It is currently under investigation whether during the 2016 U.S. elections a Russian 'troll factory', the IRA, released a number of tweets from fraudulent Twitter accounts. These tweets potentially influenced the population of voters by spreading statements, some of which were fake. The aim of this project is to better understand the strategy of the trolls by retrieving the main subjects of these tweets over time and categorizing them according to their targeted social, geographical, or political group. Quantifing the potential impact of those tweets and providing a link to specific events that were occuring in the United States at the time are the objectives. 

# Research questions

- What types of social groups were targeted
- Frequencies and characteristics of tweets preceding or succeding electoral events, mainly focusing on swing states
- What were the main topics of the fraudulent Twitter accounts over time
- What kind of strategies did the trolls use in order to influence the elections

# Dataset

The datasets we will use are two IRA tweet datasets. 
One of the [IRA tweet datasets](https://www.kaggle.com/fivethirtyeight/russian-troll-tweets/home) comprises a number of columns, including but not limited to, author ID, author, content (the tweet itself), region, language, date, following and account type, while the [second data set](https://about.twitter.com/en_us/values/elections-integrity.html#data) includes other features we would like to incorporate such as an account's creation date and the number of likes for a given tweet. We expect the types of accounts to differ in activity and subject matter depening on the timeframe. We will attempt to correlate this activity to the current events at the time. 

Datasize and format should not be an issue. The decompressed file is less than 1 GB in .csv format. 


# Ideas Dropped

- Implementing a Latent Dirichlet allocation (LDA) model for twitter topic analysis- after poor results and inconsistent topics we have chosen to switch to at the most common hashtags and using a semi-supervized learning approach consisting of training a neural network on tweets containing these hashtags. 


# Contribution of Group Members
Hannah - data exploration, Neural Network implementation, data cleaning, website.

Flavio - data exploration, data cleaning, devops for running on google colab, website.

Benjamin - data exploration, data cleaning,  website, LDA classifier.

All group members will work on the presentation


### References

[1] Hong, Liangjie, and Brian D. Davison. "Empirical study of topic modeling in twitter." Proceedings of the first workshop on social media analytics. ACM, 2010.

[2] Steinskog, Asbjørn, Jonas Therkelsen, and Björn Gambäck. "Twitter Topic Modeling by Tweet Aggregation." Proceedings of the 21st Nordic Conference on Computational Linguistics. 2017.
