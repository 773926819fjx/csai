""" 设计一个购物车处理程序，完成如下操作:
1.创建商品价格表包括商品名称，商品价格，商品内容自拟
2.创建一个购物车，购物车用于保存所购商品名称和商品价格
3.输入提示信息:购物金额上限，商品编号或选择相应的操作符(p打印,m移出,v查看,q退出)
4.当购物车内商品货款合计大于购物金额时，提示不能购买商品
5.当购物车内商品贷款合计小于购物金额时，返回重新选择购物操作
6.选择'p'打印出购物清单.包括商品名称,商品价格,购物合计金额和余额
7.选择'm'移出购买商品，首先显示购物清单，输入购买车中商品编号，删除购物车中商品，重新显示修改后购物清单
8.选择'v'查看购物清单
9.选择'q'退出购物程序 """

import csv
import sys

wlist = [['商品编号', '商品名称', '商品价格'], ['001', '可口可乐', 2.5], ['002', '百事可乐', 2.5],
         ['003', '乐事薯片原味', 4], ['004', '乐事薯片意大利红烩味', 4], ['005', '农夫山泉', 2],
         ['006', '怡宝', 2], ['007', '百岁山', 3]]
with open('商品价格表.csv', 'w', newline='', encoding='utf-8') as file:
    fwrite = csv.writer(file)
    fwrite.writerows(wlist)


def help():
    a = []
    with open('商品价格表.csv', 'r', encoding='utf-8') as F:
        fread = csv.reader(F)
        for item in fread:
            a.append(item)
            print(item)
    print("\n选择p打印出购物清单\n选择m移出购买商品\n选择v查看购物清单\n选择q退出购物程序")
    print("账户余额为10元")
    return a


class commodity:
    def __init__(self, id='', name='', price=0):
        self.id = id
        self.name = name
        self.price = price

    def __repr__(self):
        return "{}  {}".format(self.name, self.price)


class Shopping_cart:
    def print_list(self, Slist, balance=10):
        sum = 0
        for item in Slist:
            print("{}  {}".format(item.name, item.price))
            sum = sum + float(item.price)
        balance = balance - sum
        if balance < 0:
            print("余额不足，请重新购物")
            return
        else:
            print("总金额：{:.2f} 余额：{:.2f}".format(sum, balance))

    def add(self, Slist, List, id='001'):
        # id = input("请输入商品序号：")
        i = 0
        while i < len(List):
            if id == List[i][0]:
                a = commodity(List[i][0], List[i][1], List[i][2])
                Slist.append(a)
                break
            i += 1

    def remove(self, Slist):
        for item in Slist:
            print("{}  {}".format(item.name, item.price))
        id = input("请输入要删除的商品序号：")
        i = 0
        while i < len(Slist):
            if id == Slist[i].id:
                del Slist[i]
                print("删除成功!")
                break
            i += 1
        self.print_list(Slist)

    def check_list(self, Slist):
        for item in Slist:
            print(item)


if __name__ == '__main__':
    a = []
    cart = Shopping_cart()
    List = help()
    # print(List)
    cart.add(a, List, '001')
    cart.add(a, List, '002')
    cart.add(a, List, '003')
    cart.add(a, List, '004')
    while 1:
        flag = input("请输入指令：")
        if flag == 'p':
            cart.print_list(a)
            print('-------------------------------')
        elif flag == 'm':
            cart.remove(a)
            print('-------------------------------')
        elif flag == 'v':
            cart.check_list(a)
            print('-------------------------------')
        elif flag == 'q':
            sys.exit(0)
