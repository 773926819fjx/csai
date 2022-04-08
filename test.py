def divisors(n):
    """
    >>> divisors(12)
    [1, 2, 3, 4, 6]
    """
    return [x for x in range(1,n) if n%x==0]
print(divisors(12))