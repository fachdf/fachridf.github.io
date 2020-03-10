"""
    Program : WebScrapping
    Author : Fachri Dhia Fauzan
"""
post = {
    "category" : "",
    "title" : "",
    "time_published" : "",
    "get_time" : ""
}

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json

page = requests.get("https://www.republika.co.id/")
obj = BeautifulSoup(page.text,'html.parser')
data = [] #untuk nyimpan list of post (dictionary)
now = datetime.now()
time = now.strftime("%d %b %Y %H:%M:%S") #untuk get_time

for headline in obj.find_all("div",class_='conten1'):
    #Judul (title)
    post["title"] = headline.find('h2').text

    #Kategori (category)
    post["category"] = headline.find('h1').text

    #Waktu Dipublish (Terhitung dari Waktu Scrapping
    post["time_published"] = headline.find('div', class_='date').text;
    
    #Waktu Post (get_time)
    post["get_time"] = time

    data.append(dict(post))

#Write
with open("headline.json", "w") as writeJSON:
    json.dump(data, writeJSON)
    

#Tanda
print("Sedang Menulis...")

