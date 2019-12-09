import re
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
# https://www.baidu.com/s?wd=%E8%83%A1%E5%93%B2%E6%96%87
# http://localhost:63342/index02/test12/demo01/%E4%B8%AD%E6%96%87.html?_ijt=3i4jg5mrmej362eifdfobmg801
url ='http://www.baidu.com/s?'
word=input('请输入你要搜索的内容:')
# name = input('请输入你要搜索的名字：')
# age = input("请输入你要搜索的年龄:")
# sex = input('请输入你要搜索的性别:')
params = {
    'wd':word,
    # 'name':name,
    # 'age': age,
    # 'sex':sex

}
a=urllib.parse.urlencode(params)
# print(a)
final_url =url+a
# print(final_url)
data=end_url= urllib.request.urlopen(final_url)
save_file=data.read().decode()
# print(data.read().decode())
with open(word+'.html','w') as f:
    f.write(save_file)
    f.close()