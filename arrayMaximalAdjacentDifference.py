def arrayMaximalAdjacentDifference(inputArray):
    L = len(inputArray)
    max = 0
    while(L > 2 and L < 11):
        for i in range(L - 1):
            if (abs(inputArray[i] - inputArray[i + 1]) > max):
                max = abs(inputArray[i] - inputArray[i + 1])
        return max
