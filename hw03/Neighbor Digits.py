def neighbor_digits(num, prev_digit=-1):
    """
    Returns the number of digits in num that have the same digit to its right
    or left.
    >>> neighbor_digits(111)
    3
    >>> neighbor_digits(123)
    0
    >>> neighbor_digits(112)
    2
    >>> neighbor_digits(1122)
    4
    """
    "*** YOUR CODE HERE ***"
    num =list(str(num))
    count = 0
    for x in num:
        if (x == num[0]):
            count = count + 1
    for x in num[::-1]:
        if (x == num[-1]):
            count = count + 1 
    return count
        



if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)