# Are Russian Trolls Good at their Jobs? The 2016 U.S. Elections: A Timeline Analysis

# Abstract
It is currently under investigation whether during the 2016 U.S. elections a Russian 'troll factory', the IRA, released a number of tweets from fraudulent Twitter accounts. These tweets potentially influenced the population of voters by spreading statements, some of which were fake. The aim of this project is to better understand the strategy of the trolls by retrieving the main subjects of these tweets over time and categorizing them according to their targeted social, geographical, or political group. Quantifing the potential impact of those tweets and providing a link to specific events that were occuring in the United States at the time are the objectives. 

# Research questions

- What types of social groups were targeted
- Frequencies and characteristics of tweets preceding or succeding electoral events, mainly focusing on swing states
- What were the main topics of the fraudulent Twitter accounts over time
- What was the most effective strategy for the trolls (quantified by increases in followers)
- Is there a relation between the activities of trolls related to specific events and results of the elections

# Dataset

The datasets we will use are the IRA tweet datasets. We will supplement it with the final election results in different U.S. states.

One of the IRA tweet dataset comprises a number of columns, including but not limited to, author ID, author, content (the tweet itself), region, language, date, following and account type, while the second data set includes other features we would like to incorporate such as an account's creation date and the number of likes for a given tweet. We expect the types of accounts to differ in activity and subject matter depening on the timeframe. We will attempt to correlate this activity to the current events at the time. 

Datasize and format should not be an issue. The decompressed file is less than 1 GB in .csv format. 

# Pipeline

### Descriptive Statistics

The categories and types of data were investigated by referencing the Clemenson report. All columns were converted to their appropriate dtype. There were found to be no missing values, other than a few rows in the category 'account_type' which will not be used in the analysis at is a more specific version of 'account_category'.

General statistics were calculated for the dataset and were visualized in boxplots and lineplots. All visualizations are created using the interactive library Plotly which can allow for clearer views of the data. 

- The distribution of account followers by account_category was visualized using boxplots which revealed a bimodal distribution in RightTrolls and LeftTrolls. The reason for the bimodal distribution is still unclear. 
- Line plots were created to visualize the quantities of tweets over time. It is clear that there is a strong peak around the time of November 2016, when the elections were held

### Enriching and Transforming the Data

One of the objectives is to gain a better understanding of the strategies of the Russian Trolls. The subject matter of tweets and targetted audience may be useful for this endeavor. Some different filtering methods will be applied to extract the topic of a given tweet as well as its target audience.

- One filtering method that is applied is to select tweets based on the State that is mentioned. This would provide us with a summary of tweets that targetted specific States. This is of particular interest because some States are more important than others in the election - these are known as the 'Swing States' as they are not strongly democratic or republican, but rather have a tendency to 'swing' from one side to another. It may be interesting to see if the IRA took such swing states into account when sending out tweets.
- In order to do categorize the subject of a tweet, LDA, an unsupervised learning approach, is implemented. Tweets that share the same hashtag are concatenated together to create a form of 'document' which is then fed into the LDA algorithm after lemmatizing words and removing 'stop words'. Note that stop words are words which do not help distinguish topics, such as pronouns. The number of topics are a hyperparameter, along with other variables such as alpha. The final model can be visualized, and the subject matter of the topics are determined by examining the words that appear frequently in each topic.

