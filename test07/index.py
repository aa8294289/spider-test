import requests
from urllib import request

url='http://www.jingyu.com/search/stack?category=11&updateTime=0&status=0&words=0&other=0&sortBy=4&subTabType='
'''r=requests.get(url)
a=r.encoding
#print(a)
print(r.text)'''
headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'Cookie':'UM_distinctid=16d34e4a06129f-02fd1316e116ec-38607501-13c680-16d34e4a062302; __guid=8f5b51633dde0f987862d0570b5d3579.mkrom1birmc5.fjse5zyvhydi.1568550461638; test_cookie_enable=1; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216d4c52f47650a-025d45402e7a9c-38607501-1296000-16d4c52f4773a1%22%2C%22%24device_id%22%3A%2216d4c52f47650a-025d45402e7a9c-38607501-1296000-16d4c52f4773a1%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; tchannel=hypc1001; read-setting=[{%22name%22:%22read_mode%22%2C%22value%22:%22classic%22}]; CNZZDATA1261301637=2123780872-1568546137-%7C1568940339'
}




r=request.Request(url,headers=headers)