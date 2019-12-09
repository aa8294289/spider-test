# 判断网络链接是否正常
#1.获得url
import requests

# 定义一个方法，用来定义网络连接
def get_link(url):
    r = requests.head(url)
    res = r.status_code
   # print(type(res))
    if(res==200):
        print('网络链接正常！！！')

    else:
        print('网络链接失败！！！')
#get_link('http://www.baidu.com')