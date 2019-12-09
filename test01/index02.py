'''
a=[['a', 'b', 'c'], (1, 2, 3), {4, 5, 6, 7}]
for x in a:
    for y in x:
     print(y)

'''
'''a=[1, 2, 3, 4, 5, 6, 7, 8]
for x in range(1,8,2):
    print(x, end='|')
b=a[0:len(a):2]

print(b)
'''
'''
a=1.23456789
round(a,2)
print(round(a,2))
'''
'''print('please input X' )
x=input()
print('please input Y' )
y=input()
Add(x,y)'''
'''
def Add(x,y):
    result=x+y
    print('The answer is: '+result)
    return result

print('please input X' )
x=input()
print('please input Y' )
y=input()
Add(x,y)
def print(code):
    print(code)
print("hhhhh")
'''
'''def damage(skill1,skill2):
    damage1=skill1*3
    damage2=skill2*2+10
    return damage1,damage2
damages=damage(3,6)
print(damages[0],damages[1])
print(type(damages))
'''
'''
class Dog():
    """docstring for Dog."""
    name='poggy'
    age=3
    def Print_Dog(self):
        print('name:'+self.name)
        print('age:'+str(self.age))


Dog.Print_Dog(Dog)
print('================')
class Student():
    """docstring for Student."""
    name='xiaomi'
    age=18

    def Print_file(self):
        print('name:'+self.name)
        print('age:'+str(self.age))
Student.Print_file(Student)
student=Student()
print('================')
student.Print_file()'''
from test01.index01 import Human
class teacher(Human):
    """docstring for teacher."""
    name=''
    age=0
    sum=0
    score=0
    def __init__(self, name,age):

       super(teacher, self).__init__()

       self.name = name
       self.age = age
       self.score=0
       print(age)
       print(name)

    def Print_teacherfile(self):
        print('name:'+self.name)
        print('age:'+str(self.age))
    def marking(self,score):
        if score<=0:
            print('ERROR!!!!')

        else:
            self.score = score
            print('please give a score:'+str(self.score))

    @classmethod
    def plus_sum(cls):
        cls.sum+=1
        print(cls.sum)
        print('==========')
teacher1=teacher('xiatiantian', 27)
teacher.plus_sum()
teacher2=teacher('xiaobao', 28)
teacher.plus_sum()
teacher3=teacher('xuxiaoha', 29)
teacher.plus_sum()
teacher1.marking(67)
teacher2.marking(91)
teacher3.marking(0)
'''print(teacher1.age)
print(teacher1.name)'''
