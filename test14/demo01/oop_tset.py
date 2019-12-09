class car(object):
    brand ='宝马'
    color ='black'
    def run(self,s):
        print('当前行驶速度:',s+'km/s')
    def show(self,brand, color):
        print('汽车的品牌是:',car.brand,',汽车的颜色是:',car.color)
car1=car()
car1.run(str(70))
car1.show(car.brand,car.color)
