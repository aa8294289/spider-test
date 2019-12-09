import requests
from bs4 import BeautifulSoup
import json
import time
def getpositioninfo(id):
    url = 'https://www.lagou.com/jobs/%s.html' % id
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4094.1 Safari/537.36',
        'Host':'www.lagou.com',
        'Pragma':'no-cache',
        'Referer':url,
        'Upgrade-Insecure-Requests':'1'
    }
    res = requests.get(url,headers=headers)
    res.encoding = 'utf-8'
    info = BeautifulSoup(res.text, 'html.parser')
    return info.select('.job_bt')[0].text
def getpositionlist():
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4094.1 Safari/537.36',
        'Host':'www.lagou.com',
        'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'X-Anit-Forge-Code':'0',
        'X-Anit-Forge-Token':None,
        'X-Requested-With':'XMLHttpRequest'
    }
    content = []
    for i in range(1,6):
        formdata = {
            'first':'true',
            'pn':i,
            'kd':'python'
        }
        res = requests.post('https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false',headers=headers,data=formdata)
        res.encoding = 'utf-8'
        html = BeautifulSoup(res.text, 'html.parser')
        jd = json.loads(html.text)
        page_contents = jd['content']['positionResult']['result']
        for v in page_contents:
            position_dict = {
                'position_name':v['positionName'],
                'workyear':v['workYear'],
                'salary':v['salary'],
                'district':v['district'],
                'company_name':v['companyFullName']
            }
            position_id = v['positionId']
            position_detail = getpositioninfo(position_id)
            position_dict['position_detail'] = position_detail
        content.append(page_contents)
        time.sleep(5)
    line = json.dumps(content,ensure_ascii=False) #以json格式输出，不使用ascii编码
    with open('lagou.json','w') as fp:
        fp.write(line.encode('utf-8')) #写进文件以utf-8格式
if __name__=='__main__':
    getpositioninfo(5068139) #测试用