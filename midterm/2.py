sum = 0
zhen = 0
fu = 0
while 1:
    a = int(input())
    sum = sum + a
    if a > 0:
        zhen = zhen + 1
    elif a < 0:
        fu = fu + 1
    else:
        break
print(sum/(zhen + fu))
print(zhen)
print(fu)