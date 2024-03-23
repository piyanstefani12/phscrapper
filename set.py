import requests as req
from bs4 import BeautifulSoup as bs4
from pymongo import MongoClient

client = MongoClient("mongodb+srv://piyan:piyan@cluster0.oigihrz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['pornhub']
collection = db['csrapping']
linkaddr = 'https://www.pornhub.com'

def halaman1(porns):
    pornsstar = req.get(porns)
    extract = bs4(pornsstar.content, 'html.parser')
    hasil = extract.find_all("a", {"class": "gtm-event-thumb-click"})
    for i in hasil:
        if i['href'][0:5] == "/view":
            request_sub = req.get(linkaddr + i['href'])
            scrap = bs4(request_sub.content, "html.parser")
            scrap_title = scrap.find("span", {"class" : "inlineFree"}).get_text()
            scrap_view = scrap.find("span", {"class": "count"}).get_text()
            document = {
                "Link": linkaddr + i['href'],
                "Judul" : scrap_title,
                "View" : scrap_view
            }
            collection.insert_one(document)
        else:
            continue
