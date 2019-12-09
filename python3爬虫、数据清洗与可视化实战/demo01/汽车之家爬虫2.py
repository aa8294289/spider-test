# https://www.autohome.com.cn/Ashx/AjaxHeadArea.ashx?OperType=GetAreaInfo&VarName=areaData&CityId=360100
import requests
from bs4 import BeautifulSoup
first_url='https://www.autohome.com.cn/news/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
}
ids = []
data={
'OperType': 'GetAreaInfo',
'VarName': 'areaData',
'CityId': '360100',
}
r=requests.get(first_url,headers = headers, params = data)
r.encoding ='gbk'
print(r.text)
