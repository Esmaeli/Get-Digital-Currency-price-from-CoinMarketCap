import os #import OS // to clear screen
from typing import Text #to make clear screen
import requests #import request to get url
from bs4 import BeautifulSoup
from lxml import etree # to get Xpath
from unidecode import unidecode #import unidecode to convert AR / FA numbers to EN numbers
print ("Get DC price from CoinMarketCap")
getCoinMarketCapurl = input("Enter an address from CoinMarketCap website:")
os.system('cls' if os.name == 'nt' else 'clear') # clear screen code
# Get URL from CoinMarketCap
URL = getCoinMarketCapurl
# set user agents
headers = {"user-agents" : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
page = requests.get(URL , headers= headers)
# parse html page
soup = BeautifulSoup(page.content , 'html.parser')
# find title elements like Bitcoin, Ripple and...
title = soup.find(class_ = "sc-1q9q90x-0 iYFMbU h1___3QSYG").get_text()
# find abbrev like BTC, XRP and...
abbrev = soup.find(class_ = "nameSymbol___1arQV").get_text()
# find price elements
price = soup.find(class_ = "priceValue___11gHJ").get_text()
#convert arabic / farsi numbers to english numbers
in24hoursago = etree.HTML(str(soup))
in24low = etree.HTML(str(soup))
in24high = etree.HTML(str(soup))
Tradingvol = etree.HTML(str(soup))
marketvalume = etree.HTML(str(soup))
Mdom = etree.HTML(str(soup))
Mrank = etree.HTML(str(soup))
marketcap = etree.HTML(str(soup))
enprice = unidecode (price)
# print title of the product
print("Coin Name: ",title.strip())
# print price
print("Price: ", enprice.strip())
#print()
print("\nSee More Information from",title +":")
print("\n24H Price Change: ",in24hoursago.xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div[2]/div/div[1]/table/tbody/tr[2]/td/span')[0].text)
print("24H Low: ",in24low.xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div[2]/div/div[1]/table/tbody/tr[3]/td/div[1]')[0].text)
print("24h High: ",in24high.xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div[2]/div/div[1]/table/tbody/tr[3]/td/div[2]')[0].text)
print("24H Trading Volume: ",Tradingvol.xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div[2]/div/div[1]/table/tbody/tr[4]/td/span')[0].text)
print("Volume / Market Cap: ",marketvalume.xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div[2]/div/div[1]/table/tbody/tr[5]/td')[0].text)
print("Market Dominance: ",Mdom.xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div[2]/div/div[1]/table/tbody/tr[6]/td/span')[0].text)
print("Market Rank: ",Mrank.xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div[2]/div/div[1]/table/tbody/tr[7]/td')[0].text)
print("Market Cap: ",marketcap.xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/table/tbody/tr[1]/td/span')[0].text)
input("\n\n Press Enter to exit...")