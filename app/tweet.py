import gspread
from dotenv import load_dotenv
import tweepy
from os import environ
import time
from datetime import datetime, timedelta
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
load_dotenv()

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_TOKEN = environ['ACCESS_TOKEN']
ACCESS_SECRET = environ['ACCESS_SECRET']
BEARER_TOKEN = environ['BEARER_TOKEN']
INTERVAL = int(environ['INTERVAL'])
DEBUG = environ['DEBUG'] =='1'

client = tweepy.Client(bearer_token=BEARER_TOKEN, consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_SECRET)


gc = gspread.service_account(filename="cred.json")
sh = gc.open_by_key(key=environ['gckey'])
worksheet = sh.sheet1

def main():
    while True:
        tweet_records = worksheet.get_all_records()
        current_time = datetime.utcnow() + timedelta(hours=5, minutes=30)
        logger.info(f'{len(tweet_records)} tweet(s) found at {current_time.time()}')

        for idx, tweet in enumerate(tweet_records, start=2):
            msg = tweet['message']
            time_str = tweet['time']
            done = tweet['done']
            date_time_obj = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
            if not done:
                now_time_cet = datetime.utcnow() + timedelta(hours=5, minutes=30)
                if date_time_obj < now_time_cet:
                    logger.info('This should be tweeted')
                    try:
                        response = client.create_tweet(text=msg)
                        worksheet.update_cell(idx, 3, 1)
                    except Exception as e:
                        logger.warning(f'Exception during tweet! {e}')


        time.sleep(INTERVAL)

if __name__ == '__main__':
    main()