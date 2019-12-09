import requests
from bs4 import BeautifulSoup
import re

#将指定URL进行解析
def html_parse(url):
    html = requests.get(url)
    html.encoding='utf-8'
    html = html.text
    soup=BeautifulSoup(html,'lxml')
    print(soup)
# html_parse('http://www.baidu.com')




#  使用正则表达式将网页的内容提取出来

def get_url(url):
    #html_parse(url)
    htms = re.findall(r"<a.*?>.*?</a>", html_parse(url).soup.text)  # 通过正则表达式 r"<a.*?>.*?</a>" 找到所有的数据并输出

    for item in htms:
        print(item)

html_parse('http://www.baidu.com')
#get_url()
