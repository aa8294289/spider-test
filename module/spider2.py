# 爬取网页内容
from  urllib import request
def Html_spider(url):
   """

   :rtype: object
   """
   r=request.urlopen(url)
   res=r.read().decode('utf-8')
   print(res)
# 设置请求头

   headers={
       'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
   }
   r=request.Request(url,headers=headers)


#Html_spider('http://www.baidu.com')
