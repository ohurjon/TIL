def getBitValue(n, bitn):
    target_bit = 0x1 << bitn
    return 1 if (n & target_bit) != 0 else 0


def setBitValue(n, m):
    target_bit = 0x1 << m
    return n | target_bit
