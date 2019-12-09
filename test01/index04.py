from enum import Enum
from enum import IntEnum,unique
class Vip(Enum):
    YELLOw=1
    GREEN=2
    BLACK=3
    RED=4
'''print(Vip.BLACK) #Vip.BLACK
print(Vip.GREEN.value) #2
print(Vip.YELLOw.name) #YELLOw
for v in Vip:
    print(v)
# Vip.YELLOw Vip.GREEN Vip.BLACK  Vip.RED '''
a=1 #枚举转换
print(Vip(a)) #Vip.YELLOw
print('================')
@unique
class Vip1(IntEnum):
    YELLOw=1
    GREEN=1
    BLACK=3
    RED=4
print(Vip1.GREEN)


# ValueError: duplicate values found in <enum 'Vip1'>: GREEN -> YELLOw

