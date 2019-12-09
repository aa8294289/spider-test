#encoding=utf-8
from urllib3 import *
import re
http=PoolManager()
disable_warnings()
def download(url):
    r=http.request('Get',url)
    htmlStr=r.data.decode('utf-8')
    return htmlStr
#print(download('http://www.jxnu.edu.cn'))
def analyse(htmlStr):
    aList=re.findall('<a[^>]*>',htmlStr)
    result=[]
    for a in aList:
        g=re.search('href[\s]*=[\s]*[\s][\'"]([^>\'"]*)[\'"]',a)
        if g !=None:
            url=g.group(1)
            url='http://www.jxnu.edu.cn'+url
            result.append(url)
        return result
def cawler(url):
    print(url)
    html=download(url)
    urls=analyse(html)
    for url in urls:
        cawler()
cawler('http://www.jxnu.edu.cn')
