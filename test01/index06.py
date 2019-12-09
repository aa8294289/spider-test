# 匿名函数
'''f=lambda x,y:x+y

print(f(1,2))'''
#三元表达式 x if x>y else y

#map
list_x=[1,2,3,4,5,6,7,8]
def square(x):
    return x*x
'''for x in list_x:
    square(x)'''
r=map(square,list_x)
print(r.__class__)