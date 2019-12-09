import requests
import re
#http = PoolManager()
#disable_warming()

def download(url):
    result = requests.get(url)
    htmlStr = result.encoding('utf-8')
    return htmlStr
print(download('http://www.jxnu.edu.cn/'))
def analyse(htmlStr):
    aList= findall('<a[^>]*>',htmlStr)
    result=[]
    for a in aList:
        g=search('href[\s]*=[\s]*[\ '"]([^>\'""]*)[\'"]',a)
        if g!=None:
            url=g.group(1)
            url='http://www.jxnu.edu.cn/'+url
            result.append(url)
        return result
def crawler(url):
    print(url)
    html=download(url)
    urls=analyse(html)
    for url in urls:
        crawler(url)
crawler('http://www.jxnu.edu.cn/')
