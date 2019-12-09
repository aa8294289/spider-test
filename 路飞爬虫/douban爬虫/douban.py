import requests
url='https://movie.douban.com/j/chart/top_list?type=4&interval_id=100%3A90&action='
headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
}
data={
'type':'4',
'interval_id':'100:90',
'action':'',
'start':'1',
'limit':'1000',
}
r=requests.post(url=url,headers = headers, data = data)
page_json= r.json()
print(page_json)