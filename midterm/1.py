a = int(input())
b = input()
count = 0
c = []
for i in b.split():
    if count < a:
        c.append(int(i))
    count = count + 1
c.sort()
for i in c[:]:
    print(i, end = ' ')
