def makeArrayConsecutive2(statues):
    b = max(statues)
    a = min(statues)
    needed=[i for i in range(a , b + 1)]
    c = len(needed) - len(statues)
    return c
