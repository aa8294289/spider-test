class car:
    def __init__(self,brand,color) -> None:
        self.brand = brand
        self.color = color
    def run(self,s):
        print('当前行驶速度:', s + 'km/s')
    def show(self,brand, color):
        print('汽车的品牌是:',self.brand,',汽车的颜色是:',self.color)
car=car('宝马','black')