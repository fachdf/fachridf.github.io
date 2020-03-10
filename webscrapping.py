"""
    Program : WebScrapping
    Author : Fachri Dhia Fauzan
"""
post = {
    "date" : "",
    "category" : "",
    "title" : "",
    "time_published" : "",
    "get_time" : ""
}

import requests
from bs4 import BeautifulSoup
from datetime import date
import json

page = requests.get("https://www.republika.co.id/")
obj = BeautifulSoup(page.text,'html.parser')
data = []
today = date.today()
hari = today.strftime("%A, %d %B %Y") #untuk date
time = today.strftime("%d %b %Y") #untuk get_time
for headline in obj.find_all("div",class_='conten1'):
    
    #Waktu Hari Ini (date)
    post["date"] = hari

    #Kategori (category)
    post["category"] = headline.find('h1').text

    #Judul (title)
    post["title"] = headline.find('h2').text

    #Waktu Post (get_time)
    post["get_time"] = time

    #Waktu Dipublish (Terhitung dari Waktu Scrapping
    post["time_published"] = headline.find('div', class_='date').text;
    data.append(dict(post))
#Write
with open("headline.json", "w") as writeJSON:
    json.dump(data, writeJSON)
    

#Tanda
print("Sedang Menulis...")

