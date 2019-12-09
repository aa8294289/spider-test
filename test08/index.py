
from bs4 import BeautifulSoup
import requests
from requests.exceptions import RequestException
import pymysql
import json
f = open("spider.json",encoding='utf-8')
setting = json.load(f)
host = setting['host']
user = setting['user']
password = setting['password']
dbname = setting['dbname']
port = setting['port']
city = setting['city']
keyword = setting['keyword']
pagenum = setting['page']
Cookie = setting['Cookie']
def get_one_page(city, keyword, page):
   '''
   获取网页html内容并返回
   '''
   headers = {
       'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
       'Host': 'sou.zhaopin.com',
       'Referer': 'https://www.zhaopin.com/',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
       'Accept-Encoding': 'gzip, deflate',
       'Accept-Language': 'zh-CN,zh;q=0.9',
       'Cookie':Cookie
   }
   url = 'https://sou.zhaopin.com/jobs/searchresult.ashx?jl={}&kw={}&sm=0&p={}'.format(city,keyword,page)
   try:
       # 获取网页内容，返回html数据
       response = requests.get(url, headers=headers)
       # 通过状态码判断是否获取成功
       if response.status_code == 200:
           return response.text
       return None
   except RequestException as e:
       return None
def readonepage(html,db):
    cur = db.cursor()
    soup = BeautifulSoup(html,'lxml')
    for x in soup.find_all('td'):
        try:
            sybo = x.get('class')
            if sybo ==['zwmc']:
                jobname = x.div.a.get_text() #岗位名称
                jobhref = x.div.a.get('href')
                if jobhref[9] == 'i':
                    pass
                list = get_detailed(jobhref)
                list.append(jobname)
                print(jobname)
                sql = "INSERT INTO companyinfo(company_name,work_experience,edu_background,salary,describes,work_city,work_address,nature,types,scales,url,benefits,station,station_id)VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',%d)" % (
                list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7], list[8], list[9], list[10],
                list[11], list[12],counterid())
                    # try:
                cur.execute(sql)
                db.commit()
        except Exception as e:
            pass
def counterid(last=[0]):#用来存储数据库的id
    #last[0]将列表里面的第一个元素取出，然后加1，赋值给next
    next = last[0] + 1
    #修改列表里面第一个元素的值
    last[0] = next
    #返回此时运行的次数
    return next
def get_detailed(href):
    res = requests.get(href)
    soup = BeautifulSoup(res.text, 'lxml')
    for x in soup.find_all('ul'):
        try:
            sybo = x.get('class')
            # print(sybo)
            if sybo == ['terminal-ul', 'clearfix']:
                jobinfor = x.get_text()
                str = jobinfor.split('\n')
                salary = str[1].split('：')[1]#薪水
                salary = "".join(salary.split()) #去掉特殊符号
                city = str[2].split('：')[1]#城市
                exp = str[5].split('：')[1]#工作经验
                edu = str[6].split('：')[1]#学历
                # numb = str[7].split('：')[1]需求人数
        except Exception as e:
            print(e)
    for x in soup.find_all('div'):
        try:
            sybo = x.get('class')
            if sybo == ['company-box']:
                str2 = x.get_text().split('\n')
                while '' in str2:
                    str2.remove('')
                    if '查看公司地图' in str2:
                        str2.remove('查看公司地图')
                comname = str2[0]#公司名称
                scale = str2[1].split('：')[1]#企业规模
                nature = str2[2].split('：')[1]# 民营 国营
                type = str2[3].split('：')[1]# 类型：计算机/教育/so on
                place = str2[-1]#具体地址
                if len(str2) == 6:#有的公司没有网址
                    website = ' '
                else:
                    website = str2[4].split('：')[1]#公司网站
                # print(comname, scale, nature, type, place, website)
            if sybo == ['tab-inner-cont']:
                sty = x.get('style')
                if sty == None:
                    descrip = x.get_text().split('\n')[1]#工作需求
                    descrip = "".join(descrip.split())#去掉特殊符号
                    # print(descrip)
            if sybo == ['welfare-tab-box']:
                fuli=''
                for elem in x:
                    fuli = fuli + elem.string +' '
                # print(x.get_text())
        except Exception as e:
            print(e)

    return [comname,exp,edu,salary,descrip,city,place,nature,type,scale,website,fuli]

def main(city, keyword, pages):
    db = pymysql.connect(host=host, user=user , password=password, db=dbname, port=port)
    for i in range(pages):
        html = get_one_page(city, keyword, i)
        readonepage(html,db)
    db.close()


if __name__ == '__main__':
   main(city, keyword, pagenum)
