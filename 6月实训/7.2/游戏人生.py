class Preson:
    def __init__(self, power=100):
        self.power = power

    def practice(self):
        self.power += 100

    def fight(self, scenes):
        if self.judge() == False:
            print("战斗力不足已经阵亡,请前去修炼")
        else:
            if scenes == '草场':
                self.power -= 200
                if self.judge() == False:
                    print("草场战斗结束,战斗力不足阵亡")
                else:
                    print("草场战斗结束，当前战斗力为{}".format(self.power))
            elif scenes == '团战':
                self.power -= 500
                if self.judge() == False:
                    print("团战结束,战斗力不足阵亡")
                else:
                    print("团战结束，当前战斗力为{}".format(self.power))
            else:
                return

    def show(self):
        print("当前战斗力:{}".format(self.power))

    def judge(self):
        if self.power <= 0:
            return False
        else:
            return True


people = Preson(100)
i = 2
while i:
    people.practice()
    i -= 1
people.show()
people.fight('团战')
people.fight('草场')
