import requests
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        #获取服务器的响应内容，并设置最大请求时间为6秒
        res = requests.get(url, timeout = 6)
        #判断返回状态码是否为200
        res.raise_for_status()
        #设置真正的编码
        res.encoding = res.apparent_encoding
        #返回网页HTML代码
        return res.text
    except:
        return '异常'

#目标网页
url = 'http://www.jxnu.edu.cn/'

demo = getHTMLText(url)

#解析HTML代码
soup = BeautifulSoup(demo, 'html.parser')

#模糊搜索HTML代码的所有<a>标签
a_labels = soup.find_all('a')

#获取所有<a>标签中的href对应的值，即超链接
for a in a_labels:
    print(a.get('href'))
