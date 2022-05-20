def isprime(n):
    i = 2
    while i <= n**0.5:
        if n % i == 0:
            return 0
        i = i + 1
    return 1

if __name__ == "__main__":
    n = int(input())
    print(isprime(n))