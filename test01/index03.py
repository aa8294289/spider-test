import re
'''a='c|c++|java|python|html'
#b=a.index('python')
#print(b>-1)
b=re.findall('python',a)
print(b)'''

'''
a='c0c++9java7python6html'
r=re.findall('\d',a)
print(r) \d为原字符
'''
# 字符集

'''
a='abc,bcd,cde,efg,acc,afc'
r=re.findall('a[cf]c',a)
print(r)
'''
# \d 匹配数字   \D 匹配非数字
# \w 匹配单词字符 \W 匹配非单词字符
#  \s 匹配空白字符  \S 匹配非空白字符
# . 匹配除换行符\n外所有字符
# 数量级
'''a='python 1111java67php'
r=re.findall('[a-z]{3,6}',a)
print(r)    # ['python', 'java', 'php']
'''
# *匹配0次或无限次
# +匹配1次或无限次
# ？匹配0次或1次
'''a='pytho0python1pythonn2'
r=re.findall('python*',a)
s=re.findall('python+',a)
S=re.findall('python?',a)
print(r) # ['pytho', 'python', 'pythonn']
print(s) # ['python', 'pythonn']
print(S) # ['pytho', 'python', 'python']
'''

'''
# 边界匹配
qq1='100000001'
qq2='10000001'
r1=re.findall('^\d{4,8}$',qq1) #[]
r2=re.findall('^\d{4,8}$',qq2) # ['10000001']
print(r1)
print(r2)
'''
'''
#组
a='PythonPythonPythonPython'
r=re.findall('(Python){4}',a)# ['Python']
print(r)
'''
'''
#匹配模式
a='PythonC#java'
r=re.findall('c#',a,re.I)
print(r) ['C#']
'''
#re.sub 替换
'''a='PythonC#javaphp'
r=re.sub('java','Go',a)   #PythonC#Gophp
print(r)
'''

'''a='zdes23iu89gh56klp46dc32'
def convert(value):
    mached=value.group()
    if int(mached)>=6:
         return '9'
    else:
        return '0'
r=re.sub('\d',convert,a)
print(r) #zdes00iu99gh09klp09dc00
'''
s=' life is short,i use python'
r=re.findall('\w{1,6}',s)
r1=re.search('life (.*) python',s)
print(r)
print(r1.group(1))






