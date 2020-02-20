def isLucky(n):
    Tolist = [int(i) for i in str(n)]
    length = len(Tolist)
    luck1 = int( n % (10**(length/2)) )
    luck2 = int ((n - luck1)/10**(length/2))
    lucky1 = [int(i) for i in str(luck1)]
    lucky2 = [int(i) for i in str(luck2)]
    return sum(lucky1) == sum(lucky2)
