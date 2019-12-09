orgin=0
def walk(pos):
    def go(step):
        nonlocal pos
        new_pos=pos+step
        pos=new_pos
        return new_pos
    return go
man=walk(orgin)
print(man(3))
print(man(5))
print(man(7))