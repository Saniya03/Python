import requests
from bs4 import BeautifulSoup

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

def main():
    poll_xforce_exchange_rss()

if __name__ == "__main__":
    main()
