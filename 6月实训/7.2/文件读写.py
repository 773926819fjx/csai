"""将数据生成csv的文件
变量=open('filename','文件属性')
w:如果文件不存在的时候，创建文件，如果文件存在直接将原来的文件进行覆盖，重新生成一个新的文件
a+:向文件里面追加内容
r:读文件，有一个条件是必须要保证文件的存在
rb:读取二进制文件
"""
# 创建一个csv的文件
# lst1=['name','age','school','address']
# filew=open('a.csv','w')
# filew.write(','.join(lst1))
# filew.close()

import csv
import os
import pickle
from datetime import date, datetime

# filer = open('a.csv', 'r')
# lines = filer.read()
# print(lines)
# filer.close()

# datas = [['Name', 'DEP', 'Eng', 'Math', 'Chinese'],
#          ['Rose', '法学', 89, 78, 65],
#          ['Mike', '历史', 56, '', 44],
#          ['John', '数学', 45, 65, 67]]
# with open('data.csv','w',newline="")as f:
#     writer=csv.writer(f)
#     for row in datas:
#         writer.writerow(row)

# 读取文件
# ls = []
# with open('data.csv', 'r')as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(reader.line_num, row)
#         ls.append(row)
#     print(ls)

# "pickle:序列化，反序列化"
# 定义相关的函数
# 实现python序列化


def savedata(filename, filename1):
    modules = []
    m1 = {'name': "登陆注册", '描述': '使用字典保存模块名称，创建时间和模块功能信息'}
    m2 = {'name': '订单管理', "日期": date(
        2022, 7, 2), "描述": '订单管理的功能 实现的是订单数据的输入,追加，修改和删除'}
    m3 = {'name': '客户管理', '日期': datetime.now(), '描述': '使用字典保存模块的名称，创建时间和模块信息等功能'}
    modules.append(m1)
    modules.append(m2)
    modules.append(m3)

    file1 = open(filename, 'ab')
    pickle.dump(modules, file1)
    file1.close()
    file1 = open(filename, 'rb')
    lst1 = list(enumerate(pickle.load(file1), start=1))
    file1.close()
    file2 = open(filename1, 'ab')
    pickle.dump(lst1, file2)
    file2.close()
    file2 = open(filename1, 'rb')
    lst2 = pickle.load(file2)
    for x in lst2:
        print(x)
    file2.close()


# filename = input("请输入要添加行号的文件名:")
# filename1 = input("请输入新生成的文件名:")
# savedata(filename, filename1)
savedata('a.data', 'b.data')
"""通过手动输入内容，eg:请输入要添加行号的文件名，请输入新生成的文件名 ，通过文件读写的方式遍历文件并且添加行号
enumerate()"""
