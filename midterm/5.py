def isprime(n):
    i = 2
    while i <= n**0.5:
        if n % i == 0:
            return 0
        i = i + 1
    return 1

n = input()
if isprime(int(n)) and isprime(int(n[::-1])):
    print('yes')
else:
    print('no')