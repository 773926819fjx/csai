flag = input("是否为会员(是请输入Y不是请输入N)：")
number, price = map(int,input("请输入购买的数量和书的价格(用空格隔开)：").split())
if flag == 'Y':
    if number <= 5:
        print(f"需要{number * 0.85 * price}元")
    else:
        print(f"需要{number * 0.75 * price}元")
elif flag == 'N':
    if number <= 5:
        print(f"需要{number * 0.95 * price}元")
    else:
        print(f"需要{number * 0.85 * price}元")