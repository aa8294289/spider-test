import requests
from bs4 import BeautifulSoup
import re

#将指定URL进行解析
def html_parse(url):
    html = requests.get(url)
    html.encoding='utf-8'
    html = html.text
    soup=BeautifulSoup(html,'lxml')
    #print(soup)
# html_parse('http://www.baidu.com')




#  使用正则表达式将网页的内容提取出来
#1.匹配网页中的邮箱  [\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?
def get_mail(url):
    html_parse(url)
    pattern = re.compile(r'\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\.)+[A-Za-z]{2,14}')
    str = u''
    print(pattern.findall(str))

#2.匹配网页中的中文
def get_Chineseword(url):
    #pattern = "[\u4e00-\u9fa5]+"
    #[\x80 -\xff]
    html_parse(url)
    pattern = re.compile(r'[\u4e00-\u9fa5]')

    str = u''
    print(pattern.search(str))

#3 匹配网页中的url
def get_URL(url):

    # fullmatch，将regex应用到整个字串中
    # 判断一个给定的字符串是否是合法的URL
    html_parse(url)
    fullmatch_r1 = r'(https?://)?([\da-z-]+\.)+([a-z]+)/?(\w+/)*([-\.\w]+)?(\?\w+=\w+(\&\w+=\w+)*)?'
    for url in ['http://my.com?name=tt', 'http://student.shu.edu/tutor/cs/index.html',
                'https://mail.shu.edu/index.html?name=tt&age=25']:
        print(re.fullmatch(fullmatch_r1, url))
#4.判断字符串是否合法
def str_judge(url):

    # 判断一个字符串是否是合法的计算机数字表示形式
    # 正数前面可以有+，也可以没有。
    # 小数点前后都得有数字
    # 科学计数法e或者E前面得有数字，后面必须是[+-]?
    num_pattern = r'^[+-]?\d+(\.\d+)?((e|E)[+-]?\d+)?$'
    for num in ['112', '-112', '13.3', '12.3e12']:
        print(re.findall(num_pattern, num))

    for num in ['1.', '12.3e', '3e-', '2.3e12.']:
        print(re.findall(num_pattern, num))
#get_Chineseword('http://www.baidu.com')
get_URL('http://www.baidu.com')