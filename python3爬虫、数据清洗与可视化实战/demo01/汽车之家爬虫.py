import requests
from bs4 import BeautifulSoup
url='https://www.autohome.com.cn/news/'
r=requests.get(url)
r.encoding ='GBK'
# print(r.text)
soup = BeautifulSoup(r.text,'lxml')
a=soup.select('#ad_368_1 > h2 > a')
# print(a)
b=soup.select('#auto-channel-lazyload-article > ul > li> a > h3')
# print(b)
c=soup.select('#auto-channel-lazyload-article > ul > li> a')
# print(c)
d=soup.select('#auto-channel-lazyload-article > ul > li > a > div.article-pic > img')
print(d)