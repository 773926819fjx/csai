def num_eights(pos):
    """Returns the number of times 8 appears as a digit of pos.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    "*** YOUR CODE HERE ***"
    if pos % 10 == 8:
        return 1 + num_eights(pos // 10)  # 最低位为8加一
    elif pos < 10:
        return 0  # 最低位不为8且只剩最后一位或pos=0时返回0
    else:
        return num_eights(pos // 10)  # 最低位不为8且大于10递归pos//10


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
