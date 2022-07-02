class Voice:
    def __init__(self,species):
        self.species = species
    def sound(self):
        if self.species == '猫':
            print("正在模仿猫叫")
        elif self.species == '狗':
            print("正在模仿狗叫")
            
A = Voice('猫')
A.sound()
B = Voice('狗')
B.sound()