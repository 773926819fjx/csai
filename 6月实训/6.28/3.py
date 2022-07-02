import math
class MyMath:
    def __init__(self):
        self.set_R()
    
    def set_R(self):
        R = input("请输入半径：")
        if R.isdigit():
            self.__R = float(R)
            return
        print("请输入数字！")
        
    def get_C(self):
        return 2 * math.pi * self.__R
    
    def get_S(self):
        return math.pi * self.__R * self.__R
    
    def get_SA(self):
        return 4 * math.pi * self.__R * self.__R
    
    def get_V(self):
        return 4 * math.pi * self.__R * self.__R * self.__R / 3
    
    def show(self):
        print("圆的周长：{:.2f} 圆的面积：{:.2f} 球的表面积：{:.2f} 球的体积：{:.2f}".format(self.get_C(),self.get_S(),self.get_SA(),self.get_V()))
        
A = MyMath()
A.show()