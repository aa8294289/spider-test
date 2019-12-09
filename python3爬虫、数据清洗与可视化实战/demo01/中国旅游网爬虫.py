import requests
from bs4 import BeautifulSoup
url = 'http://www.cntour.cn/'
r=requests.get(url)
# print(r.text)
soup = BeautifulSoup(r.text,'lxml')
a=soup.select('#main > div > div.mtop.firstMod.clearfix > div.centerBox > ul.newsList > li> a')
# print(a)
b=soup.select('#main > div > div.mtop.firstMod.clearfix > div.leftBox > div > ul > li > a')
print(b)