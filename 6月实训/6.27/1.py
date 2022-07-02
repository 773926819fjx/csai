a = int(input("请输入月份："))
if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
    print(f"{a}月有31天")
elif a == 4 or a == 6 or a == 9 or a == 11:
    print(f"{a}月有30天")
elif a == 2:
    print(f"{a}月有28天")
else:
    print("月份输入错误，请输入1到12之间的数字")