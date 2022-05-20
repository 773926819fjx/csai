name = [x.capitalize() for x in input().split(' ')]
if len(name) <= 2 and name[0] == name[::-1][0]:
    print(name[0])
else:
    print(name[0], end=' ')
    i = 1
    while i < len(name) - 1:
        print(name[i][0], end='. ')
        i = i + 1
    print(name[len(name) - 1])