import requests
from bs4 import BeautifulSoup
url='https://www.autohome.com.cn/news/'
r= requests.get(url)
r.encoding ='gbk'
# print(r.text)
soup = BeautifulSoup(r.text,'html.parser')
tag= soup.find(id='auto-channel-lazyload-article')
li_list=tag.find('li')
for li in li_list:
    title = li.find('h3')
    print(title.text)