class SchoolPerson1:
    def __init__(self,name="",sex="",age=0):
        self.set_name(name)
        self.set_sex(sex)
        self.set_age(age)
    def set_name(self,name):
        if type(name)!=str:
            print('姓名必须是字符')
            return
        self.__name=name
    def set_sex(self,sex):
        if sex not in ['男','女']:
            print('性别必须是男或女')
            return 
        self.__sex=sex
    def set_age(self,age):
        if type(age)!=int:
            print("年龄必须为数字")
            return 
        self.__age=age
    def get_name(self):
        return self.__name
    def get_sex(self):
        return self.__sex
    def get_age(self):
        return self.__age
    def show(self):
        print("姓名:{} 性别:{} 年龄:{}".format(self.__name,self.__sex,self.__age))
        
A = SchoolPerson1("张三","男",18)
B = SchoolPerson1("王五","女",20)
A.show()
B.show()