import re
import requests
from bs4 import BeautifulSoup
import sys
url='http://www.jxnu.edu.cn/'
r=requests.get(url)
#print(r)
#print(r.text)
patten='herf='
soup=BeautifulSoup(r.text)
#print(soup)
string=soup.strings
#print(string)
a=re.search(patten,string)
print(a)