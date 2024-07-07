import requests
from database import PulseDatabase
from bs4 import BeautifulSoup

url = "https://pulse.zerodha.com/"
pulseDB = PulseDatabase()

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    news = soup.find("ul", id="news").find_all("li", class_ = "box")
    feeds = []
    for i in news:
        data = {}
        data["id"] = i.find("a")["data-id"]
        data["date"] = i.find("span", class_ = "date")["title"].split(", ")
        data["news"] = i.find("a")["href"]
        data["heading"] = i.find("a").text.strip()
        data["summary"] = i.find("div", class_ = "desc").text.strip()
        feeds.append(data)
        pulseDB.insert_pulse(data)
    print("Inserted all news in the database.")
else:
    print("Failed to retrieve data from the website.")