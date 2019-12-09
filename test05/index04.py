import requests
import re
from bs4 import BeautifulSoup
import pymysql



#解析
def parse(url):
    html=requests.get(url)
    html=html.text
    soup=BeautifulSoup(html,'lxml')
    data=soup.find_all('li', {'class': {'book', 'clearfix'}})
    for i in data:
        name=i.h3.a.text
        zz_fl=i.p.text
        zz_fl = zz_fl.split('|')
        zuoze = zz_fl[0].strip()
        fenlei = zz_fl[1].strip()
        print('书名：{0}  作者：{1}  类别：{2}'.format(name, zuoze, fenlei))
        # 将得到的数据传送给MySQL
        mysql(name, zuoze, fenlei)
        next_page(url)
def next_page(nextpage):
    a=re.search('pn=(.*)',nextpage).group(1)
    strat_url=re.findall('.*pn=',nextpage)[0]
    a=int(a)
    if a<=25:
        parse(nextpage)
    else:
        print('结束翻页')
class download_mysql:
   def __init__(self,name,zuoze,fenlei):
    self.name=name
    self.zuoze=zuoze
    self.fenlei=fenlei
    self.connect=mysql.connect(
        host='localhost',
        db='spider',
        port=3306,
        user='root',
        passwd='12345678',
        charset='utf8',
        use_unicode=False

    )
    self.cursor=self.connect.sursor()
    def save_mysql(self):























