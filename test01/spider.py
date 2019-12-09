import requests
r=requests.get("https://www.bilibili.com/")
print(r)
print(r.apparent_encoding)
print("==========")
print(r.content)
print(r.text)

'''def getHTMLtext(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "产生异常"#通用代码框架

'''