class Employee:
    def __init__(self,name="",department='computer',age=20):
        self.setName(name)
        self.setDepartment(department)
        self.setAge(age)
    def setName(self,name):
        if type(name)!=str:
            print('姓名必须是字符')
            return
        self.__name=name
    def setDepartment(self,department):
        if department not in ['computer','communcation','electric']:
            print('专业必须是computer,communcation,electric')
            return 
        self.__department=department
        
    def setAge(self,age):
        if type(age)!=int or age>=33 or age<20:
            print('年龄必须是数字，并且界于20到33之间')
            return 
        self.__age=age
    def show(self):
        print("姓名:{} 专业:{} 年龄:{}".format(self.__name,self.__department,self.__age))
        
        
class projectManager(Employee):
    def __init__(self, name, department, age):
        self.setName(name)
        self.setDepartment(department)
        self.setAge(age)

Manager1 = projectManager("Rose", "computer", 20)
Manager2 = projectManager("Mike", "electric", 30)
Manager1.show()
Manager2.show()