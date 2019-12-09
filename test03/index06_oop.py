#类和对象
#格式：class 类名称：
        #类内容
class cl1:
    pass
#print(cl1)


#实例化一个类
a=cl1()
print(a) #<__main__.cl1 object at 0x103195908>


#构造函数---初始化
#在类中的方法参数必须加self
class cl2:
    def __init__(self):
      print('hhhhhhhhh')
b=cl2()
print(b)#hhhhhhhhh <__main__.cl2 object at 0x1031a3da0>
#给类加上参数-----在构造方法中加入参数
class cl3:

    def __init__(self) :
        a=5
        b=6
        print(a+b)

c=cl3()
print(c)

class person:

    def __init__(self,name,job):
        print('my name is:'+name)
        print('my job is:'+job)

d=person('张三','老师')
print(d)
#属性：类里面的变量 self.属性名
class cl4:

    def __init__(self,name,age):
        self.Myname=name
        self.Myage=age
e=cl4('张三',78)
print(e.Myname)
print(e.Myage)
#方法：类里面的函数 def 函数名(self,...)：函数体
class cl5:
    def Get_sum(self,a , b):
        return a+b
f=cl5()
g=f.Get_sum(4,90)
print(g)
#继承（单继承，多继承）

#格式：class zi(fu): 类内容
class father():
    def speak(self):
        print('I can speak')
class mother():
    def write(self):
        print('I can write')
class son(father):
    pass
class daughter(father,mother):
    def linsten(self):
        print('I can listen')
class son2(father):

    def speak(self):
        print('I can speak 222222')

a=father()
a.speak()
b=mother()
b.write()
c=son()
c.speak()
d=daughter()
d.linsten()
e=son2()
e.speak()