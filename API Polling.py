import requests
from bs4 import BeautifulSoup
import schedule
import time

RSS_URL = "https://exchange.xforce.ibmcloud.com/rss/mal" 

def poll_xforce_exchange_rss():
    response = requests.get(RSS_URL)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "xml")
        items = soup.find_all("item")
        for item in items:
            title = item.find("title").text
            pubdate = item.find("pubDate").text
            print("Title:", title)
            print("Publication Date:", pubdate)
            print("---------------------------")
    else:
        print(f"Error: {response.status_code} - {response.text}")

def poll_weekly():
    print("Polling IBM X-Force Exchange RSS feed...")
    poll_xforce_exchange_rss()

# Schedule the weekly polling
schedule.every(1).weeks.do(poll_weekly)

while True:
    schedule.run_pending()
    time.sleep(1)
