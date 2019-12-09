import urllib.request
url='http://www.baidu.com'
headers={

    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'Cookie':'BAIDUID=2D1D7A23D64B2936DDB8120939949E9D:FG=1; PSTM=1552817055; ISSW=1; ISSW=1; BIDUPSID=612FCE5184296673458866D53A5FC867; BD_UPN=123253; sug=3; sugstore=1; bdime=0; ORIGIN=2; MCITY=-163%3A; delPer=0; BD_HOME=0; H_PS_PSSID=29654_1453_21110_29523_29720_29568_29220_26350_29588'

}
requets=urllib.request.Request(url,headers=headers)
r=urllib.request.urlopen(url)
#print(r.read().decode('utf-8'))
data=r.read().decode('utf-8')
#保存数据
with open('01-cooike.html','w') as f:
    f.write(data)