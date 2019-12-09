from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.jxnu.edu.cn/')  # 获取网页
bs = BeautifulSoup(html, 'html.parser')  # 解析网页
hyperlink = bs.find_all('a')  # 获取所有超链接
for h in hyperlink:
    hh = h.get('href')
    print(hh)