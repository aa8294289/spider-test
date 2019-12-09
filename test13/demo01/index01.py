import requests
from bs4 import BeautifulSoup
url='https://www.autohome.com.cn/news/'
r= requests.get(url)
r.encoding ='gbk'
# print(r.text)
soup = BeautifulSoup(r.text,'html.parser')
tag= soup.find(id='auto-channel-lazyload-article')
h3_list= tag.find_all('h3')
for h3 in h3_list:

    print(h3.text)
    print('============')
