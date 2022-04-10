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
    if num < 10:
        return num == prev_digit  # 如果只有一位数直接返回-1作为递归的出口
    last = num % 10  # 获取num的最低位
    rest = num // 10  # 获取num最高位
    return int(prev_digit == last or rest % 10 == last) + neighbor_digits(num // 10, last)  # 返回相同数位和


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
