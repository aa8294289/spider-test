# -*- coding: utf-8 -*-
import urllib.parse
import urllib.request
import string


def get_html():
    url='http://www.baidu.com/s?'
    prams={
        'wd':'中文',
        'key':'张',
        'values':'san'
    }
    str=urllib.parse.urlencode(prams)
   # print(str)
    final_url=url+str
    end_url= urllib.parse.quote(final_url,safe=string.printable)
    reps=urllib.request.urlopen(end_url)
    result =reps.read().decode('utf-8')
    print(result)
get_html()