import requests
url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
}

data={
'cname':'',
'pid':'',
'keyword':'北京',
'pageIndex': '2',
'pageSize':'10',
}
r=requests.post(url=url,headers=headers, data = data,)
page_text=r.text
print(page_text)
print('==============================================================================================================')
