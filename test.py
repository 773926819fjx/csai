def divisors(n):
    """
    >>> divisors(12)
    [1, 2, 3, 4, 6]
    """
    return [x for x in range(1,n) if n%x==0]


if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)