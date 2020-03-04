def palindromeRearranging(inputString):
    dict = {}
    impair = 0
    for i in inputString:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    print(dict)
    while (len(dict) < 50):
        val = list(dict.values())
        print(val)
        for v in val:
            if (v % 2 == 1):
                impair += 1
            else:
                impair += 0
        if (impair > 1):
            return False
        else:
            return True
