def sum(n):
    a = 0
    while n > 0:
        a = a + n % 10
        n = n // 10
    print(a)

x = int(input())
sum(x)
