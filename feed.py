#!/usr/bin/env python

from twitterscraper import query_tweets
import json, click, os
import datetime as dt

@click.command()
@click.option('--query', '-q', prompt='Query text', type=click.STRING, help='Keyword to query. Example: Donald Trump')
@click.option('--limit', '-l', default=None, help='Limit amount of tweet. Default: no limit')
@click.option('--exclude', '-e', default=None, help='Except keywords. For multiple keyword to exclude, use comma (,). Example: Apple, Orange')
@click.option('--start', default=(dt.date.today() - dt.timedelta(days=3)), help='Query start time. Example: 2017-12-31')
@click.option('--end', default=dt.date.today(), help='Query end time. Example: 2017-12-31')
def main(query, start, end, limit, exclude):
    clear()
    
    print("Query: %s\n" % query)

    try:
        # query result with twitter wrapper - twitterscrapper

        # Example output from twitterscraper
        # [{"fullname": "Rupert Meehl", "id": "892397793071050752", "likes": "1", "replies": "0", "retweets": "0",
        # "text": "Trump now at lowest Approval and highest Disapproval ratings ...\n\nhttps://projects.fivethirtyeight.com/", 
        # "timestamp": "2017-08-01T14:53:08", "user": "Rupert_Meehl"}]

        results = query_tweets(query, int(limit) if (limit) else limit, convertDate(start), convertDate(end))
    except:
        pass
    
    for tweet in results:
        if goodTweet(tweet.text, exclude):
            print("\033[1m %s %s \033[0m" % (tweet.user, tweet.timestamp))
            print(">> %s" % (tweet.text))
            print("\n----\n")
    

def goodTweet(text, exclude):
    # Tweet filtering
    isGoodTweet = True
    dollartagCount = 0
    hashtagCount = 0
    textList = text.replace("\n", " ").split(" ")

    if "https://" in text or "http://" in text:
        isGoodTweet = False

    if exclude and isGoodTweet:
        exceptList = exclude.replace(" ,", ",").replace(", ", ",").split(",")
        for ex in exceptList:
            if ex in text:
                isGoodTweet = False
    
    for kw in textList:
        if not isGoodTweet:
            break 

        # Ignore tweet with public ethereum address on it
        if kw.startswith("0x") and len(kw) > 30:
            isGoodTweet = False

        # Count hash tag (#)
        if kw.startswith("#"):
            hashtagCount += 1

        # Count dollar sign tag ($)
        if kw.startswith("$"):
            dollartagCount += 1

        # Skip spam msg and ads
        if hashtagCount > 5 or dollartagCount > 3:
            isGoodTweet = False
    
    return isGoodTweet

def convertDate(x):
    # Convert str date to date object format
    if isinstance(x, str):
        year, month, day = map(int, x.split("-"))
        x = dt.date(year, month, day)
        
    return x

def clear():
    # clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    main()
