def num_eights(pos):
    if pos % 10 == 8:
        return 1 + num_eights(pos // 10)  # 最低位为8加一
    elif pos < 10:
        return 0  # 最低位不为8且只剩最后一位或pos=0时返回0
    else:
        return num_eights(pos // 10)  # 最低位不为8且大于10递归pos//10


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    "*** YOUR CODE HERE ***"

    def pp(start, count, step):
        if count == n:
            return start
        elif count % 8 == 0 or num_eights(count) > 0:
            return pp(start - step, count + 1,
                      -step)  # 如果count计数满足条件，起始值减去步长，步长取反，count继续计数
        else:
            return pp(start + step, count + 1,
                      step)  # 如果count计数不满足条件，起始值加上步长，步长不变，count继续计数

    return pp(1, 1, 1)  # 初始状态，起始位置为1，计数为1，步长为1


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
