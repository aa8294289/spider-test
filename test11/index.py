# https://www.lagou.com/jobs/list_Python?px=default&city=%E5%8C%97%E4%BA%AC#filterBox
# -*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup
if __name__ == '__main__':
    url='https://www.lagou.com/jobs/list_Python?px=default&city=%E5%8C%97%E4%BA%AC#filterBox'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4094.1 Safari/537.36',
        'Host': 'www.lagou.com',
        'Pragma': 'no-cache',
        'Referer': url,
        'Upgrade-Insecure-Requests': '1'
    }
    r=requests.get(url)
    r.encoding='utf-8'
    print(r.text)