# 正则表达式
'''

原子是正则表达式中最基本的组成单位，每个正则表达式中至少要包含一个原子。
常见的原子类型有：
a普通字符作为原子
b非打印字符作为原子
c通用字符作为原子
d原子表
'''
# 普通字符作为原子
import re
string='sghgjsghj'
patten='sgh'
a=re.search(patten,string)
print(a) # <re.Match object; span=(0, 3), match='sgh'>
# 非打印字符作为原子
# \n,\t,
string='sghg\njsghj'
patten='\n'
a=re.search(patten,string)
print(a) # <re.Match object; span=(4, 5), match='\n'>
# 通用字符作为原子
# \d 匹配数字   \D 匹配非数字
# \w 匹配单词字符 \W 匹配非单词字符
#  \s 匹配空白字符  \S 匹配非空白字符
# . 匹配除换行符\n外所有字符
string='sg34657543hg\njsghj'
patten='\d'
a=re.search(patten,string)
print(a) #<re.Match object; span=(2, 3), match='3'>
b=re.findall(patten,string)
print(b) #['3', '4', '6', '5', '7', '5', '4', '3']