import tweepy
import schedule
import time
from utils import get_nvidia_price
from api import tweet_price

def job():
    price = get_nvidia_price()
    print(f"NVIDIA Current Price: {price}")
    tweet_price(price)

def main():
    job()
    #schedule.every().day.at("09:00").do(job)  # Schedule the job every day at 9 AM

    #while True:
    #    schedule.run_pending()
    #    time.sleep(1)

if __name__ == "__main__":
    main()