import mysql.connector

import requests

from bs4 import BeautifulSoup
mydb=mysql.connector.connect(
    host="localhost",
    user='root',
    password='Badhri'
)


mycur=mydb.cursor()

mycur.execute("Use scrap")
# res=requests.get("https://techcrunch.com/category/cryptocurrency/")
# soup=BeautifulSoup(res.content,'html.parser')
# crypto=soup.find_all('a',class_="post-block__title__link")
# crypto_txt=[]
# for i in crypto:
#     x=i.text
#     crypto_txt.append(x)
# crypto_links=[]
# for i in crypto:
#     x=i.get("href")
#     crypto_links.append(x)

# print(crypto_txt)
# print(crypto_links)

# c1="Insert into scrap_data(title,link)"
# c2=f"values ({crypto_txt},{crypto_links})"

# mycur.execute(c1,c2)

