def front(s,f):
    """
    >>> front(range(10), lambda x:x % 2 == 1)
    [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
    """
    return [x for x in s if f(x)] +[x for x in s if not f(x)]

if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)