import requests
url ='http://www.sogou.com/web'
wd=input('请输入你要搜索的信息:')
params = {
    'query':wd,
}
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
}
r= requests.get(url=url,params=params,headers = headers)
r.encoding ='utf-8'
page_text=r.text
filename = wd+'.html'
with open(filename,'w') as fp:
    fp.write(page_text)
    fp.close()
print('爬取成功！！！')
