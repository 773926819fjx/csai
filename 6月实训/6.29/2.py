class Student:
    def __init__(self,Id = '0',name = '',curriculum = ''):
        self.Id = Id
        self.name = name
        self.curriculum = curriculum
    
    def __repr__(self):
        return "id={} name={} curriculum={}".format(self.Id,self.name,self.curriculum)

class Student_management_system():
    def add(self,student):
        Id = input("请输入Id：")
        name = input("请输入name：")
        curriculum = input("请输入课程：")
        S = Student(Id,name,curriculum)
        student.append(S)
        
    def delete(self,student):
        Id = input("请输入要删除的学生序号：")
        i = 0
        while i<len(student):
            if Id == student[i].Id:
                del student[i]
                print("删除成功!")
                break
            i += 1
            
    def modify(self,student):
        Id = input("请输入要修改的学生序号：")
        i = 0
        while i<len(student):
            if Id == student[i].Id:
                Id = input("请输入修改后的Id：")
                name = input("请输入修改后的name：")
                curriculum = input("请输入修改后的课程：")
                S = Student(Id,name,curriculum)
                student[i] = S
                print("修改成功!")
                break
            i += 1
            
    def find(self,student):
        Id = input("请输入要查找的学生序号：")
        i = 0
        while i<len(student):
            if Id == student[i].Id:
                print(student[i])
                print("查找成功!")
                break
            i += 1

            
student = []
A = Student_management_system()
A.add(student)
A.add(student)
A.delete(student)
A.modify(student)
A.find(student)