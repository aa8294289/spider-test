import requests
url ='https://fanyi.baidu.com/sug'
word=input('请输入你要翻译的英文单词：')
data={
    'kw': word,

}
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
}
r=requests.post(url=url,data=data,headers=headers)
print(r.json())

