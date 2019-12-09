# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse

def get_html():
    url = 'http://www.baidu.com'
    a=urllib.request.urlopen(url)
    file=a.read().decode('utf-8')
    print(file)
    with open('baidu.html','w')as f:
        f.write(file)
        f.close()
# def save_file():
# #     file=get_html().file
# #     with open('baidu.html','w',) as f:
# #         f.write(file)
# #         f.close()
# # get_html()
# # save_file()
get_html()