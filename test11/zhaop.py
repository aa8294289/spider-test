import re
import urllib.request
import urllib.parse
import ssl


headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'Host': 'www.lagou.com',
    'Cookie':'JSESSIONID=ABAAABAAADEAAFID5E1F6870EE9940B6527957642CC66D2; WEBTJ-ID=20191006103520-16d9eebdbfae7-07efea47bbf829-1d3d6b55-1296000-16d9eebdbfb4ab; _ga=GA1.2.1426144341.1570329321; _gid=GA1.2.765973881.1570329321; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1570329321; user_trace_token=20191006103520-f1016f1a-e7e1-11e9-a53a-5254005c3644; LGSID=20191006103520-f101716c-e7e1-11e9-a53a-5254005c3644; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fs%3Ftn%3D02003390_43_hao_pg%26isource%3Dinfinity%26iname%3Dbaidu%26itype%3Dweb%26ie%3Dutf-8%26wd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGUID=20191006103520-f101733d-e7e1-11e9-a53a-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_search; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1570329330; LGRID=20191006103529-f671c13b-e7e1-11e9-a53a-5254005c3644; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216d9eec014371a-06d25ac839e2b1-1d3d6b55-1296000-16d9eec0144a38%22%2C%22%24device_id%22%3A%2216d9eec014371a-06d25ac839e2b1-1d3d6b55-1296000-16d9eec0144a38%22%7D; sajssdk_2015_cross_new_user=1; X_HTTP_TOKEN=f4a8fae57acde09364392307513629f445b4e5cd96; SEARCH_ID=5503e451231645cf9ba5faf7b231f6ab'

}
data={
    'first':'true',
    'pn':1,
    'kd':'python'
}
context = ssl._create_unverified_context()
# req = request.Request(url=url, headers=headers)
# res = request.urlopen(req, context=context)



url='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
req=urllib.request.Request(url,headers=headers,data=urllib.parse.urlencode(data).encode('utf-8'),method='POST')
resp=urllib.request.urlopen(req,context=context)
print(resp.read().decode('utf-8'))


