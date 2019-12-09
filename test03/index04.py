# 文件操作
# 打开
#open(文件地址，" 文件操作")
#文件操作：
#'w':写
#'r':读
#'a'：添加
#'b':二进制操作
#读取
file=open('/Users/wangjian/Desktop/学习资料/小说/文本1.txt','r')
#print(file)
fh=file.read()
data=file.readline()
#print(fh)
print(data)
#文件写入
data='hhhhhhh'
file2=open('/Users/wangjian/Desktop/学习资料/小说/文本3.txt','w')
file2.write(data)
file2.close()
data2='aaa'
file2=open('/Users/wangjian/Desktop/学习资料/小说/文本3.txt','a+')
file2.write(data2)
file2.close()


#关闭文件
file_c = file.close()
