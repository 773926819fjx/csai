class SchoolPerson2:
    def __init__(self,name="",sex="",age=0):
        self.set_name(input("请输入姓名："))
        self.set_sex(input("请输入性别："))
        self.set_age(int(input("请输入年龄：")))
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
    def __del__(self):
        print("对象被清除!")
        
A = SchoolPerson2()
B = SchoolPerson2()
A.show()
B.show()
del A
del B

class Student(SchoolPerson2):
    def __init__(self):
        self.set_name(input("请输入姓名："))
        self.set_sex(input("请输入性别："))
        self.set_age(int(input("请输入年龄：")))
        self.set_class(input("请输入班级："))
        self.set_sno(input("请输入学号："))

    def set_class(self, Class):
        self.__class = Class

    def set_sno(self, sno):
        self.__sno = sno

    def get_class(self):
        return self.__class

    def get_sno(self):
        return self.__sno

    def print_student(self):
        print("姓名:{} 性别:{} 年龄:{} 班级:{} 学号:{}".format(self.get_name(),
              self.get_sex(), self.get_age(), self.get_class(), self.get_sno()))


class Teacher(SchoolPerson2):
    def __init__(self):
        self.set_name(input("请输入姓名："))
        self.set_sex(input("请输入性别："))
        self.set_age(int(input("请输入年龄：")))
        self.set_department(input("请输入部门："))
        self.set_cno(input("请输入工号："))

    def set_department(self, department):
        self.__department = department

    def set_cno(self, cno):
        self.__cno = cno

    def get_department(self):
        return self.__department

    def get_cno(self):
        return self.__cno

    def print_teacher(self):
        print("姓名:{} 性别:{} 年龄:{} 部门:{} 工号:{}".format(self.get_name(
        ), self.get_sex(), self.get_age(), self.get_department(), self.get_cno()))


a = Student()
b = Teacher()
a.print_student()
b.print_teacher()
