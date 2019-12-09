import urllib.request
url='http://www.baidu.com'
headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
requets=urllib.request.Request(url,headers=headers)
r=urllib.request.urlopen(url)
#print(r.read().decode('utf-8'))
data=r.read().decode('utf-8')
#保存数据
with open('01-cooike.html','w') as f:
    f.write(data)