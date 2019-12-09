import urllib.request
'''r=urllib.request.urlopen('http://www.baidu.com')
print(r.read().decode('utf-8'))'''
import urllib.parse
'''data=bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8')
r=urllib.request.urlopen('http://httpbin.org/post',data=data)
print(r.read())'''
r=urllib.request.urlopen('http://httpbin.org/get',timeout=1)
print(r.read())