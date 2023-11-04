import pandas as pd
from tqdm.notebook import tqdm
import snscrape.modules.twitter as sntwitter


negative_hashtags=['#depression', '#anxiety', '#mentalhealth', '#sadquote', '#sad', '#mentalillness', '#mentalhealthmatters', 
                   '#selfcare', '#suicide', '#therapy', '#depressed', '#recovery', '#stress', '#health', '#trauma', '#die', 
                   '#sadness', '#psychology', '#pain', '#depressionhelp', '#broken', '#iquit', '#notfeelingwell', '#sheleftme']
negative_tweets=[]
n_tweets= 1000
for hashtags in negative_hashtags:
    scraper= sntwitter.TwitterSearchScraper(hashtags)
    
    for i, tweet in tqdm(enumerate(scraper.get_items()),total=n_tweets):
        data=[tweet.id, tweet.rawContent]
        negative_tweets.append(data)

        if i>n_tweets:
            break
    
    


positive_hashtags=['#fitness', '#happiness', '#goals', '#happybirthday', '#lifestyle', '#positive', '#hope', '#friends', '#love',
                 '#motivation', '#life', '#success', '#health', '#positivity', '#smile', '#positivethinking', '#gym', '#inspiration',
                 '#god','#thank', '#today', '#good', '#sunday', '#beautiful', '#holiday','#beautiful', '#nevergiveup', '#happy', '#goodvibes', 
                 '#believe', '#positivevibes', '#joy', '#goodday', '#feelingood',]
positive_tweets=[]
for hashtags in positive_hashtags:
    scraper= sntwitter.TwitterSearchScraper(hashtags)
   
    for i, tweet in tqdm(enumerate(scraper.get_items()),total=n_tweets):
        data=[tweet.id, tweet.rawContent]
        positive_tweets.append(data)

        if i>n_tweets:
            break

negative_tweet_df=pd.DataFrame(negative_tweets, columns=["id","tweet"])
negative_tweet_df['label']=1
positive_tweet_df=pd.DataFrame(positive_tweets, columns=["id","tweet"])
positive_tweet_df['label']=0

dataset=negative_tweet_df.append(positive_tweet_df)
dataset.to_csv('tweeets_dataset.csv', index=False)