import requests
from bs4 import BeautifulSoup  # Beautiful Soup是一个可以从HTML或XML文件中提取结构化数据的Python库

# 要爬的网页
url = "http://www.jxnu.edu.cn/"
# 构造头文件，模拟浏览器访问,否则访问个别网页会出现403错误
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
# 用requests库中的gete方法向网页发送请求
page = requests.get(url)
# 获取html
html = page.text
# print(html)
# 将获取到的内容转换成BeautifulSoup格式，并将html.parser作为解析器
soup = BeautifulSoup(html, 'html.parser')

# 查找html中所有a标签中class='linkto'的语句，所查找到的内容返回到变量titles中
titles = soup.find_all('a')

# open()是读写文件的函数,with语句会自动close()已打开文件
with open(r"/Users/wangjian/Desktop/index02/test04\aaa.text", "w", encoding='utf-8') as file:  # 在D盘中打开/创建一个名为 aaa 的txt文件
    for title in titles:  # 遍历titles中的每个元素
       # file.write(title.string + '\n')  # 向文件中写入title的字符串(即文章的标题)，并换行
        file.write(title.get('href') + '\n\n')  # 向文件中写入文章的链接，并两次换行
