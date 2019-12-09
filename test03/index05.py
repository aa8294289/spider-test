#异常处理
'''
异常处理格式
try:
    程序
except Exception as 异常名称:
    异常处理
'''
try:
    for i in range(1,10):
        print(i)
        if(i==4):
            print('ok')

    print('hhhhh')
except Exception as err:
    print(err)
#让异常后的程序继续
for i in range(1,10):
    try:
        print(i)
        if(i==4):
            print('ok')
    except Exception as err:
        print(err)
print('hhhhh')
